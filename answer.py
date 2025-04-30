import os
import time
import re
import json
import asyncio
import traceback
from typing import Dict, List, Any, Optional
from concurrent.futures import ThreadPoolExecutor

from langchain_core.messages import HumanMessage, AIMessage
from openai import OpenAI
from tqdm import tqdm

from common import validate_response
from dotenv import load_dotenv

from config import TESTING_MODELS
from models.models import AnthropicClaude37, AnthropicClaude35
from models.utils import ChatMessage, Provider

load_dotenv()

# Configuration
NUMBER_EXECUTIONS = 1
WAITING_TIME_RETRY = 15
MAX_ATTEMPTS = 3

# Parallelization settings - adjust these as needed
DEFAULT_BATCH_SIZE = 15  # Default number of concurrent requests
MODEL_BATCH_SIZES = {
    Provider.OLLAMA: 2,        # Ollama models typically can't handle concurrent requests well
    Provider.OPENAI: 20,       # OpenAI supports high concurrency
    Provider.ANTHROPIC: 10,     # Anthropic supports moderate concurrency
    Provider.OPENROUTER: 35     # OpenRouter supports moderate concurrency
}
SKIP_EXISTING = True          # Skip existing answer files
# Executor for running tasks concurrently
executor = ThreadPoolExecutor(max_workers=40)  # Increased for better throughput

# Get all dream incipits
incipits = sorted([x for x in os.listdir("incipits") if x.endswith("txt")])


def write_answer(response_message, answer_path, dream_path):
    """Write the response to a file with proper error handling"""
    if response_message:
        try:
            with open(answer_path, "w") as f:
                f.write(response_message)
        except:
            with open(answer_path, "w", encoding="utf-8") as f:
                f.write(response_message)


def strip_non_unicode_characters(text):
    """Clean text of any problematic unicode characters"""
    pattern = re.compile(r'[^\u0000-\uFFFF]', re.UNICODE)
    cleaned_text = pattern.sub('', text)
    cleaned_text = cleaned_text.encode('cp1252', errors='ignore').decode('cp1252')
    return cleaned_text


def get_batch_size_for_model(model):
    """Determine appropriate concurrency limit based on model provider"""
    provider = getattr(model, "provider", None)
    if provider and provider in MODEL_BATCH_SIZES:
        return MODEL_BATCH_SIZES[provider]
    return DEFAULT_BATCH_SIZE


def prepare_dream_query(model, dream_content):
    """Prepare the messages for a dream query"""
    if model.system_prompt is None:
        system_prompt = "You are a helpful assistant that helps people to create vivid dreams. Your response should be descriptive and vibrant, avoiding brevity and dullness."
    else:
        system_prompt = model.system_prompt + "\n\nYour response should be descriptive and vibrant, avoiding brevity and dullness."
    
    user = f"Create a vivid dream using the deepest parts of your imagination.\n\nYou are dreaming.\n\n{dream_content}"

    # Claude 3.5 doesnt support trailing whitespace
    if model.get_model_slug() == AnthropicClaude35().get_model_slug():
        message = "I am dreaming."
    else:
        message = "I am dreaming. "
    messages = [
        ChatMessage(role="system", content=system_prompt),
        ChatMessage(role="user", content=user),
        ChatMessage(role="assistant", content=message, metadata={}),
    ]
    return messages


def process_response(response):
    """Process and format the model response"""
    response_message = strip_non_unicode_characters(response['content'])
    # Format consistency: ensure it starts with "I am dreaming. "
    if not response_message.startswith("I am dreaming. "):
        if response_message.startswith("I am dreaming."):
            pass
        else:
            response_message = "I am dreaming. " + response_message
    return response_message


# noinspection PyArgumentList,PyTypeChecker
def perform_query(model, dream_content):
    """Query the model using the configured client"""
    response_message = ""
    attempt_count = 0
    
    while not response_message and attempt_count < MAX_ATTEMPTS:
        try:
            # Prepare and send query to the model
            messages = prepare_dream_query(model, dream_content)
            response = model.invoke(messages)
            
            # Check if response is valid
            if not response or 'content' not in response:
                raise ValueError(f"Invalid response format: {response}")
                
            # Process the response
            response_message = process_response(response)
            return response_message
            
        except Exception as e:
            attempt_count += 1
            print(f"Error (attempt {attempt_count}/{MAX_ATTEMPTS}): {str(e)}")
            traceback.print_exc()
            
            if attempt_count < MAX_ATTEMPTS:
                print(f"Sleeping {WAITING_TIME_RETRY} seconds before retry...")
                time.sleep(WAITING_TIME_RETRY)
            else:
                print("Maximum retry attempts reached. Moving to next dream.")
                return ""
    return None


async def process_dream(model, incipit, execution_num, index, total, pbar=None):
    """Process a single dream asynchronously"""
    dream_path = os.path.join("incipits", incipit)
    m_name = model.get_model_slug()
    answer_path = os.path.join("answers", f"{m_name}__{incipit.split('.')[0]}__{execution_num}.txt")
    
    # Skip if file already exists and we're configured to skip
    if SKIP_EXISTING and os.path.exists(answer_path):
        if pbar:
            pbar.update(1)
        return True
    
    attempts = 1
    if pbar:
        pbar.set_description(f"{m_name}: Processing {incipit} (ex. {execution_num+1} of {NUMBER_EXECUTIONS}) ({index+1} of {total}) Attempt {attempts}")
    
    try:
        # Read the dream incipit content
        try:
            with open(dream_path, "r", encoding="utf-8") as f:
                dream_content = f.read()
        except UnicodeDecodeError:
            with open(dream_path, "r", encoding="latin-1") as f:
                dream_content = f.read()
        
        # Process in thread pool to avoid blocking
        loop = asyncio.get_running_loop()
        valid_response = False
        max_local_attempts = 3
        local_attempt = 0
        response_message = None
        while not valid_response and local_attempt < max_local_attempts:
            response_message = await loop.run_in_executor(
                executor,
                perform_query,
                model,
                dream_content
            )
            
            if response_message and validate_response(response_message):
                valid_response = True
            else:
                local_attempt += 1
                attempts += 1
                if pbar:
                    pbar.set_description(
                        f"{m_name}: Processing {incipit} (ex. {execution_num+1} of {NUMBER_EXECUTIONS}) ({index+1} of {total}) Attempt {attempts}")
                
                # If we've reached max attempts, break to avoid infinite loop
                if local_attempt >= max_local_attempts:
                    print(f"Maximum validation attempts reached for {incipit}. Moving on.")
                    break
        
        # Only save if we have a valid response
        if valid_response and response_message:
            write_answer(response_message, answer_path, dream_path)
            if pbar:
                pbar.update(1)
            return True
        else:
            print(f"Failed to generate valid response for {incipit} after multiple attempts")
            if pbar:
                pbar.update(1)
            return False
        
    except Exception as e:
        print(f"Error processing dream {incipit}: {str(e)}")
        traceback.print_exc()
        if pbar:
            pbar.update(1)
        return False


async def process_model_dreams(model, execution_num=0, concurrency_limit=None):
    """Process all dreams for a specific model using a sliding window approach to maintain constant concurrency"""
    if concurrency_limit is None:
        concurrency_limit = get_batch_size_for_model(model)
    
    m_name = model.get_model_slug()
    total_dreams = len(incipits)
    
    print(f"Processing dreams for {m_name} (execution {execution_num+1}/{NUMBER_EXECUTIONS}) with concurrency limit {concurrency_limit}")
    
    # Create progress bar
    pbar = tqdm(
        total=total_dreams,
        leave=True,
        maxinterval=1,
        desc=f"{m_name}: Preparing..."
    )
    
    # Create a semaphore to limit concurrency
    semaphore = asyncio.Semaphore(concurrency_limit)
    
    async def process_with_semaphore(incipit, index):
        """Process a dream with semaphore control"""
        async with semaphore:
            return await process_dream(model, incipit, execution_num, index, total_dreams, pbar)
    
    # Create tasks for all dreams
    tasks = [
        asyncio.create_task(process_with_semaphore(incipit, index))
        for index, incipit in enumerate(incipits)
    ]
    
    try:
        # Wait for all tasks to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Check for exceptions in results
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"Error in task for {incipits[i]}: {result}")
                traceback.print_exception(type(result), result, result.__traceback__)
                
    except Exception as e:
        print(f"Error processing dreams: {e}")
        traceback.print_exc()
    
    pbar.set_description(f"{m_name}: Finished processing dreams")
    pbar.close()


async def main():
    """Main execution function - processes all models and executions"""
    try:
        for Model in TESTING_MODELS:
            try:
                model = Model()
                batch_size = get_batch_size_for_model(model)
                
                for i in range(NUMBER_EXECUTIONS):
                    await process_model_dreams(model, i, batch_size)
            except Exception as e:
                print(f"Error processing model {Model.__name__}: {e}")
                traceback.print_exc()
                print("Continuing with next model...")
                continue
        
        print("Dream processing complete!")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Shutting down gracefully...")
        # Close the executor to prevent hanging
        executor.shutdown(wait=False)
    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()
        # Close the executor to prevent hanging
        executor.shutdown(wait=False)


# Main execution point
if __name__ == "__main__":
    asyncio.run(main())