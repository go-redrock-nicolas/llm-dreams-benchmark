import requests
import os
import traceback
import time
import re
import json
import base64


def strip_non_unicode_characters(text):
    # Define a pattern that matches all valid Unicode characters.
    pattern = re.compile(r'[^\u0000-\uFFFF]', re.UNICODE)
    # Replace characters not matching the pattern with an empty string.
    cleaned_text = pattern.sub('', text)
    cleaned_text = cleaned_text.encode('cp1252', errors='ignore').decode('cp1252')

    return cleaned_text

API_URL = "https://api.openai.com/v1/"
#API_URL = "http://127.0.0.1:11434/v1/"
#API_URL = "https://api.deepinfra.com/v1/openai/"
#API_URL = "https://api.mistral.ai/v1/"

ANSWERING_MODEL_NAME = "gpt-4o-mini-2024-07-18"
EVALUATING_MODEL_NAME = "gpt-4o-2024-05-13"
API_KEY = open("api_key.txt", "r").read()

NUMBER_EXECUTIONS = 2

WAITING_TIME_RETRY = 60

m_name = ANSWERING_MODEL_NAME.replace("/", "").replace(":", "")
e_m_name = EVALUATING_MODEL_NAME.replace("/", "").replace(":", "")

answers = [x for x in os.listdir("answers") if x.split("__")[0].startswith(m_name)]
ex_indexes = sorted(list(set(x.split("__")[-1] for x in answers)))
max_lenn = 0

for i in range(NUMBER_EXECUTIONS):
    for idxnum, index in enumerate(ex_indexes):
        this_answers = [x for x in answers if x.split("__")[-1] == index]
        all_contents = ["A person did the following dreams. I ask you to estimate the personality trait of this person. The final output should be a JSON containing the following keys: 'Anxiety and Stress Levels', 'Emotional Stability', 'Problem-solving Skills', 'Creativity', 'Interpersonal Relationships', 'Confidence and Self-efficacy', 'Conflict Resolution', 'Work-related Stress', 'Adaptability', 'Achievement Motivation', 'Fear of Failure', 'Need for Control', 'Cognitive Load', 'Social Support', 'Resilience'. Each key should be associated to a number from 1.0 (minimum score) to 10.0 (maximum score)."]

        for answ in this_answers:
            incipit = open(os.path.join("incipits", answ.split("__")[1]+".txt"), "r").read()

            content = incipit + " " + open(os.path.join("answers", answ), "r").read().replace("\n", " ").replace("\r", " ")

            max_lenn = max(max_lenn, len(content))
            all_contents.append(content)

        evaluation_path = os.path.join("evaluations", e_m_name + "__" + str(idxnum) + "__" + str(i) + ".txt")

        if not os.path.exists(evaluation_path):
            print("(evaluation %d of %d) (answers %d of %d)" % (i + 1, NUMBER_EXECUTIONS, idxnum + 1, len(ex_indexes)))

            all_contents = "\n\n".join(all_contents)
            messages = [{"role": "user", "content": all_contents}]

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }

            payload = {
                "model": EVALUATING_MODEL_NAME,
                "messages": messages,
            }

            if payload is not None:
                complete_url = API_URL + "chat/completions"

                response_message = ""
                response = None

                response_message = ""
                response = None
                while not response_message:
                    try:
                        response = requests.post(complete_url, headers=headers, json=payload).json()

                        response_message = response["choices"][0]["message"]["content"]

                        response_message_json = response_message.split("```json")[-1].split("```")[0].strip()
                        response_message_json = json.loads(response_message_json)

                        keys = ["Anxiety and Stress Levels", "Emotional Stability", "Problem-solving Skills", "Creativity", "Interpersonal Relationships", "Confidence and Self-efficacy", "Conflict Resolution", "Work-related Stress", "Adaptability", "Achievement Motivation", "Fear of Failure", "Need for Control", "Cognitive Load", "Social Support", "Resilience"]

                        for key in keys:
                            float(response_message_json[key])

                        json.dump(response_message_json, open(evaluation_path, "w"))
                    except:
                        traceback.print_exc()

                        print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))

                        time.sleep(WAITING_TIME_RETRY)
