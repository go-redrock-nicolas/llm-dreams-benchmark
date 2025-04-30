import os
import time
import re
import json
import traceback
import numpy as np
import pyperclip
import subprocess
import sys
from tempfile import NamedTemporaryFile

from langchain_core.messages import HumanMessage
from openai import OpenAI
from tqdm import tqdm

from common import (
    EVALUATING_MODEL_NAME, EVALUATION_FOLDER,
    MANUAL, COUNCIL_ENABLED, COUNCIL_MODELS,
    get_model_identifier, QUALITIES_TO_OBSERVE, OBSERVATION_MAP
)
from config import ANSWERING_MODEL_NAME #, TESTING_MODELS
from models.base_model import BaseModel
from models.models import OpenAIGPT41, AnthropicClaude37, Qwen3b235a22
from models.utils import human_message

NUMBER_EXECUTIONS = 2
WAITING_TIME_RETRY = 17

# Directory to store intermediate council evaluations
COUNCIL_INTERMEDIATES_DIR = "council_intermediates"

TESTING_MODELS = [
    Qwen3b235a22
]

class Shared:
    answering_model_name = ANSWERING_MODEL_NAME
    evaluating_model_name = EVALUATING_MODEL_NAME


def strip_non_unicode_characters(text):
    # Define a pattern that matches all valid Unicode characters.
    pattern = re.compile(r'[^\u0000-\uFFFF]', re.UNICODE)
    # Replace characters not matching the pattern with an empty string.
    cleaned_text = pattern.sub('', text)
    cleaned_text = cleaned_text.encode('cp1252', errors='ignore').decode('cp1252')

    return cleaned_text


def __validate(xx):
    keys = QUALITIES_TO_OBSERVE

    for key in keys:
        float(xx[key])


def __fix_commas(xx):
    xx = xx.split("\n")
    yy = [xx[0]]
    for i in range(1, len(xx)-1):
        row = xx[i]
        if not row.endswith(",") and i < len(xx)-2:
            row = row + ","
        yy.append(row)
    yy.append(xx[-1])
    return "\n".join(yy)


def __fix_problems(xx):
    keys = QUALITIES_TO_OBSERVE

    def levenshtein_distance(s1, s2):
        if len(s1) < len(s2):
            return levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[len(s2)]

    result = {}
    xx_keys = list(xx.keys())

    for target_key in keys:
        if not xx_keys:  # If input dictionary is empty
            result[target_key] = None
            continue

        # Find the key in xx with minimum edit distance to target_key
        closest_key = min(xx_keys, key=lambda k: levenshtein_distance(target_key.lower(), k.lower()))
        result[target_key] = xx[closest_key]

    return result


def interpret_response(response_message0):
    response_message = response_message0
    if "```json" in response_message:
        response_message = response_message.split("```json")[-1]

    returned = None
    response_message_json = response_message.split("```")
    for msg in response_message_json:
        if msg.strip() == "":
            continue
        msg = msg.strip()
        xx = json.loads(msg)

        returned = xx

    if returned is not None:
        return returned

    response_message = response_message0
    if "{" in response_message and "}" in response_message:
        response_message = response_message.split("{")[-1].split("}")[0]
        response_message = "{\n" + response_message.strip() + "\n}"
        response_message = __fix_commas(response_message)
        response_message = json.loads(response_message)
        response_message = __fix_problems(response_message)
        __validate(response_message)
        return response_message

    raise Exception("Failed to interpret response")


# Initialize OpenAI client for OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=None,  # Will be set later
    timeout=120.0,
    max_retries=2,
)


def get_evaluation(text, model: BaseModel):
    """Get evaluation from a specific model using the OpenAI library"""

    result = model.invoke(
        message_input=[
            human_message(content=text),
        ]
    )

    return interpret_response(result['content'])


def get_council_evaluation(text, m_name, idxnum, i, pbar, current_message, category):
    """Get evaluations from all council models and average the results"""
    if not os.path.exists(COUNCIL_INTERMEDIATES_DIR):
        os.makedirs(COUNCIL_INTERMEDIATES_DIR)
    
    results = {}
    
    # Get evaluations from each model in the council
    for model in COUNCIL_MODELS:
        model_obj = model()
        model_id = model_obj.get_model_slug()

        #print(f"Getting evaluation from {model_obj.get_model_slug()}")
        pbar.set_description(f"{current_message} Evaluator {model_id}")

        attempt = 0
        max_attempts = 3
        success = False
        model_result = None
        while attempt < max_attempts and not success:
            try:
                model_result = get_evaluation(text, model_obj)
                success = True

            except Exception as e:
                attempt += 1
                # print(
                #     f"Error getting evaluation from {model_obj.get_model_slug()} (attempt {attempt}/{max_attempts}): {str(e)}")
                if attempt < max_attempts:
                    time.sleep(WAITING_TIME_RETRY)
                else:
                    #print(f"Failed to get evaluation from {model_obj.get_model_slug()} after {max_attempts} attempts.")
                    model_result = None

        if not model_result:
            # If we couldn't get an evaluation from this model, skip it
            #print(f"Skipping {model_obj.get_model_slug()} due to persistent errors")
            continue
        else:
            results[model_id] = model_result

    averaged_results = {}

    if not results:
        # If we couldn't get results from any model, throw an exception
        raise Exception("Failed to get evaluations from any council models")

    # we can save the intermediate results now to the files per model
    for model_id, keys in results.items():
        with open(os.path.join(COUNCIL_INTERMEDIATES_DIR, f"{m_name}__{idxnum}__{i}_{model_id}.json"), "w") as f:
            json.dump(results[model_id], f)
        for key, value in keys.items():
            if key not in averaged_results:
                averaged_results[key] = results[model_id][key]
            else:
                averaged_results[key] = str(
                    (float(averaged_results[key]) + float(value)))

    # Now average the results
    for key, value in OBSERVATION_MAP[category].items():
        averaged_results[key] = str(
            round(float(averaged_results[key]) / len(results), 2))
    # Ensure all required keys are present
    for key, value in OBSERVATION_MAP[category].items():
        if key not in averaged_results:
            averaged_results[key] = "0.0"  # Default middle value for missing keys
    
    return averaged_results


def perform_evaluation():
    # Load API key
    for MODEL in TESTING_MODELS:
        MODEL = MODEL()
        m_name = MODEL.get_model_slug()
        answering_model_name = m_name
        ret = False
        # Get list of answers for this model
        answers = [x for x in os.listdir("answers") if x.split("__")[0].startswith(m_name)]
        ex_indexes = sorted(list(set(x.split("__")[-1] for x in answers)))

        for i in range(NUMBER_EXECUTIONS):
            for idxnum, index in enumerate(ex_indexes):
                # Get individual answers for this execution index
                this_answers = sorted([x for x in answers if x.split("__")[-1] == index])
                
                # Process each dream individually
                pbar = tqdm(enumerate(this_answers), f"Processing answers for model {m_name}")
                for dream_idx, answer_file in pbar:
                    # Generate unique path for each individual dream evaluation
                    evaluation_path = os.path.join(
                        EVALUATION_FOLDER, 
                        f"{m_name}__{str(idxnum)}__{str(i)}_dream{dream_idx}.json"
                    )
                    pbar.set_description(f"Processing answers for model {m_name}")
                    
                    if os.path.exists(evaluation_path):
                        print(f"ALREADY DONE (dream {dream_idx+1} of {len(this_answers)}) (evaluation {i+1} of {NUMBER_EXECUTIONS}) (answers {idxnum+1} of {len(ex_indexes)})",
                              answering_model_name, "council" if COUNCIL_ENABLED else Shared.evaluating_model_name)
                        continue
                    
                    #print(f"(dream {dream_idx+1} of {len(this_answers)}) (evaluation {i+1} of {NUMBER_EXECUTIONS}) (answers {idxnum+1} of {len(ex_indexes)})",
                          #answering_model_name, "council" if COUNCIL_ENABLED else Shared.evaluating_model_name)
                    
                    try:
                        # Read incipit and answer files
                        incipit = open(os.path.join("incipits", answer_file.split("__")[1] + ".txt"), "r", encoding="utf-8").read()
                        
                        try:
                            answer_content = open(os.path.join("answers", answer_file), "r").read().replace("\n", " ").replace("\r", " ")
                        except:
                            answer_content = open(os.path.join("answers", answer_file), "r", encoding="utf-8").read().replace("\n", " ").replace("\r", " ")

                        dream_content = (
                            "Prompt:\n"
                            f"{incipit}\n\n"
                            "Answer:\n"
                            f"{answer_content}"
                        )
                        result_dict = {}
                        for CATEGORY, ITEMS in OBSERVATION_MAP.items():
                            pbar.set_description(message := f"Processing answers for model {m_name} ({CATEGORY})")
                            instruction_guide = "For each trait you are looking for, the following guidance is provided:\n\n"
                            #take the list of ITEMS and concatenate into a list of single quoted strings
                            item_list = ""
                            for trait, instructions in ITEMS.items():
                                item_list = item_list + "'" + trait + "'" + ", "
                                instruction_guide = instruction_guide + trait + ":\n" + instructions + "\n\n"
                            # now remove the last ", "
                            item_list = item_list[:-2]


                            prompt = (
                                "You are evaluating a single dream to determine the personality traits revealed in it. "
                                "You will estimate the personality traits based on this specific dream. "
                                f"The category of personality traits to be observed is: {CATEGORY}. "
                                "The final output should be a JSON object containing the following keys: "
                                
                                f"{item_list}"
                                
                                "Each key should be associated to a number from 0.0 (undetectable, unknown, or not applicable) to 10.0 (maximum score). "
                                "If a trait cannot be determined, it should be assigned a value of 0.0.\n"
                                "Your output must be ONLY a JSON object with the keys listed above. Do not preface the output with a message, no matter how helpful you may think it is.\n\n"
                                
                                f"{instruction_guide}"
                                
                                f"Dream content: \n{dream_content}"
                            )

                            response_message_json = get_council_evaluation(
                                prompt,
                                m_name,
                                f"{idxnum}_dream{dream_idx}",
                                i,
                                pbar,
                                message,
                                CATEGORY
                            )
                            # we will be squishing all the fields from the resulting json into our result_dict
                            for key in response_message_json:
                                result_dict[key] = response_message_json[key]

                        if result_dict:
                            json.dump(result_dict, open(evaluation_path, "w"))
                            ret = True

                    except Exception as e:
                        print(f"Error processing dream {dream_idx} (file: {answer_file}): {str(e)}")
                        traceback.print_exc()
                        continue

    return ret


if __name__ == "__main__":
    if not os.path.exists(EVALUATION_FOLDER):
        os.mkdir(EVALUATION_FOLDER)
    
    if not os.path.exists(COUNCIL_INTERMEDIATES_DIR):
        os.mkdir(COUNCIL_INTERMEDIATES_DIR)

    perform_evaluation()