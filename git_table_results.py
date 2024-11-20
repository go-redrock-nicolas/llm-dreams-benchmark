import json
import os
import numpy as np
import pandas as pd
from copy import copy


evaluations = [x for x in os.listdir("evaluations") if x.endswith(".txt")]

creation_time = []
for ev in evaluations:
    full_path = os.path.join("evaluations", ev)
    creation_time.append((ev, os.path.getctime(full_path)))
creation_time = sorted(creation_time, key=lambda x: (x[1], x[0]))

llms = []
all_llms_scores = {}

individual_results = []
overall_results = []
individual_results.append("## Individual Results")
overall_results.append("## Overall Results\n")

for ct in creation_time:
    llm = ct[0].split("__")[0]

    if llm not in llms:
        llms.append(llm)

for llm in llms:
    evaluations = [x for x in os.listdir("evaluations") if x.split("__")[0] == llm]

    keys = ["Anxiety and Stress Levels", "Emotional Stability", "Problem-solving Skills", "Creativity",
            "Interpersonal Relationships", "Confidence and Self-efficacy", "Conflict Resolution", "Work-related Stress",
            "Adaptability", "Achievement Motivation", "Fear of Failure", "Need for Control", "Cognitive Load",
            "Social Support", "Resilience"]

    scores = {k: [] for k in keys}

    for ev in evaluations:
        full_path = os.path.join("evaluations", ev)

        dictio = json.load(open(full_path, "r"))

        for k in keys:
            scores[k].append(dictio[k])

    for k in keys:
        v = scores[k]
        scores[k] = (round(np.mean(v), 1), round(np.std(v), 1))
        scores[k] = str(scores[k][0])+" $\\pm$ "+str(scores[k][1])

    these_scores = copy(scores)
    all_llms_scores[llm] = these_scores

    values = [scores[k] for k in keys]

    dataframe = pd.DataFrame({"Personality Trait": keys, "Score (1.0-10.0)": values})
    stru = dataframe.to_markdown(index=False)
    individual_results.append("\n")
    individual_results.append("### " + llm)
    individual_results.append("\n")
    individual_results.append(stru)
    individual_results.append("\n\n\n")

llms = sorted(llms, key=lambda x: x.lower())

overall_columns = {"LLM": llms}

for k in keys:
    overall_columns[k] = [all_llms_scores[llm][k] for llm in llms]

dataframe = pd.DataFrame(overall_columns)
stru = dataframe.to_markdown(index=False)
overall_results.append(stru)

combined_stru = "\n".join(overall_results)+"\n"+"\n".join(individual_results)

F = open("results_gpt_4o_2024_05_13.md", "w")
F.write(combined_stru)
F.close()
