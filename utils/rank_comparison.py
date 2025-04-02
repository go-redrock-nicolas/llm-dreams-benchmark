import os
from scipy.stats import pearsonr
import pandas as pd


def interpret(content):
    llm_scores = {}

    content = "".join(content.split("|:--")[1:])
    content = content.split("\n")[1:]
    #print(content)
    for row in content:
        if "## Individual" in row:
            break

        row = row.split("|")
        model = row[1].strip()
        mhs = float(row[2].replace("*", ""))
        llm_scores[model] = mhs

    return llm_scores


JUDGES = {
    "gpt-4.5-preview": interpret(open(os.path.join("..", "results_gpt_45.md"), "r").read()),
    "mistral-small-2503": interpret(open(os.path.join("..", "alt_results_mistral-small-2503.md"), "r").read()),
    "qwen2.5-32b": interpret(open(os.path.join("..", "alt_results_qwen25-32b.md"), "r").read()),
}

for judge in JUDGES:
    model_keys = list(JUDGES[judge].keys())
    break

for judge in JUDGES:
    JUDGES[judge] = [(k, JUDGES[judge][k]) for k in model_keys]
    JUDGES[judge] = [x[1] for x in JUDGES[judge]]

dataframe = []

for judge in JUDGES:
    row = {"Model": judge}
    summ = 0
    for judge2 in JUDGES:
        corr, pv = pearsonr(JUDGES[judge], JUDGES[judge2])
        row[judge2] = corr
        summ += corr
    row["SUM"] = summ
    dataframe.append(row)

dataframe = pd.DataFrame(dataframe)
dataframe.sort_values(["SUM", "Model"], ascending=False, inplace=True)

dataframe.to_markdown("../stats/JUDGES_RANK.md", index=False)
