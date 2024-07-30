import requests
import os
import traceback
import time
import re
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

MODEL_NAME = "gpt-4o-mini-2024-07-18"
API_KEY = open("api_key.txt", "r").read()

NUMBER_EXECUTIONS = 2

WAITING_TIME_RETRY = 60

incipits = [x for x in os.listdir("incipits") if x.endswith("txt")]

m_name = MODEL_NAME.replace("/", "").replace(":", "")

for i in range(NUMBER_EXECUTIONS):
    for index, incipit in enumerate(incipits):
        print(incipit+" (ex. %d of %d) (incipit %d of %d)" % (i+1, NUMBER_EXECUTIONS, index+1, len(incipits)))

        dream_path = os.path.join("incipits", incipit)
        answer_path = os.path.join("answers", m_name+"__"+incipit.split(".")[0]+"__"+str(i)+".txt")

        if not os.path.exists(answer_path):
            messages = [{"role": "user", "content": "You are dreaming. Can you complete the following dream?\n\n"+open(dream_path, "r").read()}]

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }

            payload = {
                "model": MODEL_NAME,
                "messages": messages,
                "max_tokens": 4096
            }

            if payload is not None:
                complete_url = API_URL + "chat/completions"

                response_message = ""
                response = None

                while not response_message:
                    try:
                        response = requests.post(complete_url, headers=headers, json=payload).json()

                        response_message = strip_non_unicode_characters(response["choices"][0]["message"]["content"])

                        F = open(answer_path, "w")
                        F.write(response_message)
                        F.close()
                    except:
                        print(response)

                        traceback.print_exc()

                        print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))

                        time.sleep(WAITING_TIME_RETRY)
