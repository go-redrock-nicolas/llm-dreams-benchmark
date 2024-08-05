import os
import pyperclip
import subprocess

incipits_folder = "../incipits"
answers_folder = "../answers"

incipits = [x for x in os.listdir(incipits_folder) if x.endswith("txt")]

model_name = input("Give me the name of the model that you are testing -> ")

count = 0
while True:
    for inc in incipits:
        dream_path = os.path.join(incipits_folder, inc)

        dream = "You are dreaming. Can you complete the following dream?\n\n"+open(dream_path, "r").read()
        pyperclip.copy(dream)

        response_path = os.path.join(answers_folder, model_name+"__"+inc.split(".")[0]+"__"+str(count)+".txt")
        print(response_path)

        F = open(response_path, "w")
        F.close()

        subprocess.run(["notepad.exe", response_path])

        input("Press ENTER to continue")

    prompt = input("Continue? (Y/N)")

    if prompt != "Y":
        break

    count += 1
