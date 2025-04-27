import os
import time
import re
import json
import traceback
from openai import OpenAI
from tqdm import tqdm

from common import validate_response
from dotenv import load_dotenv

from config import TESTING_MODELS

load_dotenv()

NUMBER_EXECUTIONS = 5
WAITING_TIME_RETRY = 15

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


# noinspection PyArgumentList,PyTypeChecker
def perform_query(text):
    """Query the model using the OpenAI SDK"""
    response_message = ""
    attempt_count = 0
    max_attempts = 3
    
    while not response_message and attempt_count < max_attempts:
        try:
            # Create a completion using the native OpenAI SDK

            response = MODEL.invoke(text)
            
            # Extract and clean the response text
            response_message = strip_non_unicode_characters(response.content)
            return response_message
            
        except Exception as e:
            attempt_count += 1
            print(f"Error (attempt {attempt_count}/{max_attempts}): {str(e)}")
            traceback.print_exc()
            
            if attempt_count < max_attempts:
                print(f"Sleeping {WAITING_TIME_RETRY} seconds before retry...")
                time.sleep(WAITING_TIME_RETRY)
            else:
                print("Maximum retry attempts reached. Moving to next dream.")
                return ""
    return None


# Main execution loop

for Model in TESTING_MODELS:
    MODEL = Model()
    m_name = MODEL.get_model_slug()
    client = MODEL
    for i in range(NUMBER_EXECUTIONS):
        while True:
            try:
                pbar = tqdm(
                    iterable=sorted(enumerate(incipits)),
                    leave=True,
                    maxinterval=1,

                )
                for index, incipit in pbar:
                    attempts = 1
                    pbar.set_description(f"{m_name}: Processing {incipit} (ex. {i+1} of {NUMBER_EXECUTIONS}) ({index+1} of {len(incipits)}) Attempt {attempts}")

                    dream_path = os.path.join("incipits", incipit)
                    answer_path = os.path.join("answers", f"{m_name}__{incipit.split('.')[0]}__{i}.txt")

                    if not os.path.exists(answer_path):
                        # Read the dream incipit content
                        try:
                            with open(dream_path, "r", encoding="utf-8") as f:
                                dream_content = f.read()
                        except UnicodeDecodeError:
                            with open(dream_path, "r", encoding="latin-1") as f:
                                dream_content = f.read()

                        while True:
                            # Generate the response
                            prompt = f"You are dreaming. Complete the following dream:\n\n{dream_content}"
                            response_message = perform_query(prompt)

                            if response_message and validate_response(response_message):
                                break
                            attempts += 1
                            pbar.set_description(
                                f"{m_name}: Processing {incipit} (ex. {i + 1} of {NUMBER_EXECUTIONS}) ({index + 1} of {len(incipits)}) Attempt {attempts}")

                        # Save the response
                        write_answer(response_message, answer_path, dream_path)
                        #pbar.set_description(f"  ✓ Dream response saved to {answer_path}")

                    pbar.set_description(f"{m_name}: Finished processing dreams")
                break
            except Exception as e:
                print(f"Error processing dreams batch: {str(e)}")
                traceback.print_exc()
                print(f"Sleeping {WAITING_TIME_RETRY} seconds before retrying batch...")
                time.sleep(WAITING_TIME_RETRY)

    print("Dream processing complete!")