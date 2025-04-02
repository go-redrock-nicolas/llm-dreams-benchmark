import requests
import os
import traceback
import time
import re
import json
import pyperclip
import subprocess
import sys
from tempfile import NamedTemporaryFile
from common import ANSWERING_MODEL_NAME, EVALUATING_MODEL_NAME, EVALUATION_FOLDER, EVALUATION_API_URL, MANUAL

API_URL = EVALUATION_API_URL

API_KEY = open("judge_api_key.txt", "r").read()

NUMBER_EXECUTIONS = 2

WAITING_TIME_RETRY = 17


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
    keys = ["Anxiety and Stress Levels", "Emotional Stability", "Problem-solving Skills", "Creativity",
            "Interpersonal Relationships", "Confidence and Self-efficacy", "Conflict Resolution",
            "Work-related Stress", "Adaptability", "Achievement Motivation", "Fear of Failure",
            "Need for Control", "Cognitive Load", "Social Support", "Resilience"]

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
    keys = ["Anxiety and Stress Levels", "Emotional Stability", "Problem-solving Skills", "Creativity",
            "Interpersonal Relationships", "Confidence and Self-efficacy", "Conflict Resolution",
            "Work-related Stress", "Adaptability", "Achievement Motivation", "Fear of Failure",
            "Need for Control", "Cognitive Load", "Social Support", "Resilience"]

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
        try:
            msg = msg.strip()
            xx = json.loads(msg)
            xx = __fix_problems(xx)

            __validate(xx)

            returned = xx
        except:
            pass

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

    raise Exception("Fail")


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
            response = requests.post(complete_url, headers=headers, json=payload)
            #print(response)
            #print(response.status_code)
            #print(response.text)
            response = response.json()
            response_message = response["candidates"][0]["content"]["parts"][0]["text"]
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


def get_evaluation_openai_new(text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": Shared.evaluating_model_name,
        "input": text
    }

    complete_url = API_URL + "responses"

    response = requests.post(complete_url, headers=headers, json=payload)
    if response.status_code != 200:
        print(response)
        print(response.status_code)
        print(response.text)

    response = response.json()
    response_message = response["output"][-1]["content"][0]["text"]
    response_message_json = interpret_response(response_message)

    return response_message_json


def get_evaluation(text):
    if "api.openai" in API_URL:
        return get_evaluation_openai_new(text)
    elif "googleapis" in API_URL:
        return get_evaluation_google(text)
    else:
        return get_evaluation_openai(text)


def perform_evaluation(answering_model_name):
    ret = False
    m_name = answering_model_name.replace("/", "").replace(":", "")

    answers = [x for x in os.listdir("answers") if x.split("__")[0].startswith(m_name)]
    ex_indexes = sorted(list(set(x.split("__")[-1] for x in answers)))
    max_lenn = 0

    for i in range(NUMBER_EXECUTIONS):
        for idxnum, index in enumerate(ex_indexes):
            this_answers = [x for x in answers if x.split("__")[-1] == index]
            all_contents = [
                "A person did the following dreams. I ask you to estimate the personality trait of this person. The final output should be a JSON containing the following keys: 'Anxiety and Stress Levels', 'Emotional Stability', 'Problem-solving Skills', 'Creativity', 'Interpersonal Relationships', 'Confidence and Self-efficacy', 'Conflict Resolution', 'Work-related Stress', 'Adaptability', 'Achievement Motivation', 'Fear of Failure', 'Need for Control', 'Cognitive Load', 'Social Support', 'Resilience'. Each key should be associated to a number from 1.0 (minimum score) to 10.0 (maximum score). Please follow strictly the provided JSON schema in the evaluation!"]

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

            evaluation_path = os.path.join(EVALUATION_FOLDER, m_name + "__" + str(idxnum) + "__" + str(i) + ".txt")

            if not os.path.exists(evaluation_path):
                print("(evaluation %d of %d) (answers %d of %d)" % (
                    i + 1, NUMBER_EXECUTIONS, idxnum + 1, len(ex_indexes)), answering_model_name,
                      Shared.evaluating_model_name)

                all_contents = "\n\n".join(all_contents)

                response_message_json = None
                if not MANUAL:
                    response_message_json = get_evaluation(all_contents)
                else:
                    msg_len = len(all_contents)

                    if msg_len < sys.maxsize:
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
                    ret = True
            else:
                print("ALREADY DONE (evaluation %d of %d) (answers %d of %d)" % (
                    i + 1, NUMBER_EXECUTIONS, idxnum + 1, len(ex_indexes)), answering_model_name,
                      Shared.evaluating_model_name)
    return ret


if __name__ == "__main__":
    if not os.path.exists(EVALUATION_FOLDER):
        os.mkdir(EVALUATION_FOLDER)

    if False:
        cont = True
        while cont:
            try:
                cont = False
                available_models = {x.split("__")[0] for x in os.listdir("answers") if not "init" in x}
                for m in available_models:
                    xy = perform_evaluation(m)
                    cont = cont or xy
            except:
                time.sleep(WAITING_TIME_RETRY)
                cont = True
    else:
        perform_evaluation(Shared.answering_model_name)
