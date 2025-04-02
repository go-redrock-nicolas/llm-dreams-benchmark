ANSWERING_MODEL_NAME = "qwen2.5-omni-7b"
EVALUATING_MODEL_NAME = "gpt-4.5-preview"
EVALUATING_MODEL_NAME = "qwen-2.5-32b"


def get_evaluation_folder():
    if "gpt-4.5" in EVALUATING_MODEL_NAME:
        return "evaluations-gpt45"
    elif "qwen-2.5-32b" in EVALUATING_MODEL_NAME:
        return "evaluations-qwen25-32b"


def get_git_table_result():
    if "gpt-4.5" in EVALUATING_MODEL_NAME:
        return "results_gpt_45.md"
    elif "qwen-2.5-32b" in EVALUATING_MODEL_NAME:
        return "alt_results_qwen25-32b.md"


def get_evaluation_api_url():
    if "gpt-4.5" in EVALUATING_MODEL_NAME:
        return "https://api.openai.com/v1/"
    elif "qwen-2.5-32b" in EVALUATING_MODEL_NAME:
        return "https://api.groq.com/openai/v1/"


EVALUATION_FOLDER = get_evaluation_folder()
TARGET_GIT_TABLE_RESULT = get_git_table_result()
EVALUATION_API_URL = get_evaluation_api_url()
