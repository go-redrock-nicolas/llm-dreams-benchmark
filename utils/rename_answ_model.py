import os


def do_renaming(base_path, original_name, novel_name):
    files = [x for x in os.listdir(base_path) if x.startswith(original_name)]

    for f in files:
        original_path = os.path.join(base_path, f)
        new_path = original_path.replace(original_name, novel_name)

        print(original_path, new_path, os.path.exists(original_path), os.path.exists(new_path))
        os.rename(original_path, new_path)


if __name__ == "__main__":
    original_name = "chatgpt-4o-latest_"
    novel_name = "chatgpt-4o-latest-2024-11-20_"

    do_renaming("../answers", original_name, novel_name)
    do_renaming("../evaluations", original_name, novel_name)


