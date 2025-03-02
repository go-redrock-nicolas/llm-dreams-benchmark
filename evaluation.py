import requests
import os
import traceback
import time
import re
import json
import pyperclip
import subprocess
from tempfile import NamedTemporaryFile
from common import ANSWERING_MODEL_NAME, EVALUATING_MODEL_NAME

API_URL = "https://api.openai.com/v1/"
# API_URL = "http://127.0.0.1:11434/v1/"
# API_URL = "https://api.deepinfra.com/v1/openai/"
# API_URL = "https://api.mistral.ai/v1/"
# API_URL = "https://generativelanguage.googleapis.com/v1beta/"

API_KEY = open("judge_api_key.txt", "r").read()

NUMBER_EXECUTIONS = 2

WAITING_TIME_RETRY = 60

MANUAL = True


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


def interpret_response(response_message):
    response_message_json = response_message.split("```json")[-1].split("```")[0].strip()
    response_message_json = json.loads(response_message_json)

    keys = ["Anxiety and Stress Levels", "Emotional Stability", "Problem-solving Skills", "Creativity",
            "Interpersonal Relationships", "Confidence and Self-efficacy", "Conflict Resolution",
            "Work-related Stress", "Adaptability", "Achievement Motivation", "Fear of Failure",
            "Need for Control", "Cognitive Load", "Social Support", "Resilience"]

    for key in keys:
        float(response_message_json[key])

    return response_message_json


def get_evaluation_google(text):
    complete_url = API_URL + "models/" + Shared.evaluating_model_name + ":generateContent?key=" + API_KEY

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {"parts": [
                {"text": text}
            ]}
        ]
    }

    response_message = ""
    response = None

    while not response_message:
        try:
            response = requests.post(complete_url, headers=headers, json=payload).json()
            response_message = response["choices"][0]["message"]["content"]
            response_message_json = interpret_response(response_message)
            return response_message_json
        except:
            traceback.print_exc()
            print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))
            time.sleep(WAITING_TIME_RETRY)


def get_evaluation_openai(text):
    messages = [{"role": "user", "content": text}]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": Shared.evaluating_model_name,
        "messages": messages,
    }

    complete_url = API_URL + "chat/completions"

    response_message = ""
    response = None

    while not response_message:
        try:
            response = requests.post(complete_url, headers=headers, json=payload).json()
            response_message = response["choices"][0]["message"]["content"]
            response_message_json = interpret_response(response_message)
            return response_message_json
        except:
            traceback.print_exc()
            print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))
            time.sleep(WAITING_TIME_RETRY)


def get_evaluation(text):
    if "googleapis" in API_URL:
        return get_evaluation_google(text)
    else:
        return get_evaluation_openai(text)


def perform_evaluation(answering_model_name):
    m_name = answering_model_name.replace("/", "").replace(":", "")

    answers = [x for x in os.listdir("answers") if x.split("__")[0].startswith(m_name)]
    ex_indexes = sorted(list(set(x.split("__")[-1] for x in answers)))
    max_lenn = 0

    for i in range(NUMBER_EXECUTIONS):
        for idxnum, index in enumerate(ex_indexes):
            this_answers = [x for x in answers if x.split("__")[-1] == index]
            all_contents = [
                "A person did the following dreams. I ask you to estimate the personality trait of this person. The final output should be a JSON containing the following keys: 'Anxiety and Stress Levels', 'Emotional Stability', 'Problem-solving Skills', 'Creativity', 'Interpersonal Relationships', 'Confidence and Self-efficacy', 'Conflict Resolution', 'Work-related Stress', 'Adaptability', 'Achievement Motivation', 'Fear of Failure', 'Need for Control', 'Cognitive Load', 'Social Support', 'Resilience'. Each key should be associated to a number from 1.0 (minimum score) to 10.0 (maximum score)."]

            for answ in this_answers:
                incipit = open(os.path.join("incipits", answ.split("__")[1] + ".txt"), "r", encoding="utf-8").read()

                try:
                    content = incipit + " " + open(os.path.join("answers", answ), "r").read().replace("\n",
                                                                                                      " ").replace("\r",
                                                                                                                   " ")
                except:
                    content = incipit + " " + open(os.path.join("answers", answ), "r", encoding="utf-8").read().replace(
                        "\n", " ").replace("\r", " ")

                max_lenn = max(max_lenn, len(content))
                all_contents.append(content)

            evaluation_path = os.path.join("evaluations", m_name + "__" + str(idxnum) + "__" + str(i) + ".txt")

            if not os.path.exists(evaluation_path):
                print("(evaluation %d of %d) (answers %d of %d)" % (
                    i + 1, NUMBER_EXECUTIONS, idxnum + 1, len(ex_indexes)), answering_model_name,
                      Shared.evaluating_model_name)

                all_contents = "\n\n".join(all_contents)

                response_message_json = None
                if not MANUAL:
                    response_message_json = get_evaluation(all_contents)
                else:
                    pyperclip.copy(all_contents)

                    temp_file = NamedTemporaryFile(suffix=".txt")
                    temp_file.close()
                    F = open(temp_file.name, "w")
                    F.close()
                    subprocess.run(["notepad.exe", temp_file.name])

                    F = open(temp_file.name, "r")
                    response_message = F.read().strip()
                    F.close()

                    response_message_json = interpret_response(response_message)
                    #print(response_message_json)
                if response_message_json:
                    json.dump(response_message_json, open(evaluation_path, "w"))
            else:
                print("ALREADY DONE (evaluation %d of %d) (answers %d of %d)" % (
                    i + 1, NUMBER_EXECUTIONS, idxnum + 1, len(ex_indexes)), answering_model_name,
                      Shared.evaluating_model_name)


if __name__ == "__main__":
    if False:
        available_models = {x.split("__")[0] for x in os.listdir("answers") if not "init" in x}
        for m in available_models:
            perform_evaluation(m)
    else:
        perform_evaluation(Shared.answering_model_name)
