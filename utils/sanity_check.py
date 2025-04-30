import os
from collections import Counter

base_path = ".."

answering_models = [x.split("_")[0] for x in os.listdir(os.path.join(base_path, "answers")) if x.split("_")[0]]
answering_models = Counter(answering_models)

for m in answering_models:
    if answering_models[m] != 30:
        print("answering_models", m, answering_models[m])

evaluation_models = set()
evaluations_models_counter = {}

evaluation_folders = [x for x in os.listdir(base_path) if x.startswith("evaluations-")]

for ev in evaluation_folders:
    eval_models = [x.split("_")[0] for x in os.listdir(os.path.join(base_path, ev)) if x.split("_")[0]]
    eval_models = Counter(eval_models)

    evaluation_models.update(set(eval_models))
    evaluations_models_counter[ev] = eval_models

diff1 = set(answering_models).difference(evaluation_models)
diff2 = evaluation_models.difference(set(answering_models))

if diff1:
    raise Exception("more answering models: "+str(diff1))

if diff2:
    raise Exception("more evaluation models: "+str(diff2))

for ev in evaluation_folders:
    for mod in evaluations_models_counter[ev]:
        if evaluations_models_counter[ev][mod] != 4:
            print(ev, mod, evaluations_models_counter[ev][mod])
