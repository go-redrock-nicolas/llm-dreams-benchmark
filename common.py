ANSWERING_MODEL_NAME = "openrouter/optimus-alpha"
EVALUATING_MODEL_NAME = "gpt-4.5-preview"
# EVALUATING_MODEL_NAME = "qwen-2.5-32b"
# EVALUATING_MODEL_NAME = "mistral-small-2503"
# EVALUATING_MODEL_NAME = "chatgpt-4o-latest"
# EVALUATING_MODEL_NAME = "grok-2-1212"
# EVALUATING_MODEL_NAME = "gemini-2.0-flash"
# EVALUATING_MODEL_NAME = "claude-3-5-sonnet-20241022"


def get_evaluation_folder():
    if "gpt-4.5" in EVALUATING_MODEL_NAME:
        return "evaluations-gpt45"
    elif "qwen-2.5-32b" in EVALUATING_MODEL_NAME:
        return "evaluations-qwen25-32b"
    elif "mistral-small-2503" in EVALUATING_MODEL_NAME:
        return "evaluations-mistral-small"
    elif "gpt-4o" in EVALUATING_MODEL_NAME:
        return "evaluations-gpt4o"
    elif "grok-2" in EVALUATING_MODEL_NAME:
        return "evaluations-grok2"
    elif "gemini-2.0-flash" in EVALUATING_MODEL_NAME:
        return "evaluations-gemini2-flash"
    elif "claude-3-5-sonnet" in EVALUATING_MODEL_NAME:
        return "evaluations-claude-35-sonnet"


def get_git_table_result():
    if "gpt-4.5" in EVALUATING_MODEL_NAME:
        return "results_gpt_45.md"
    elif "qwen-2.5-32b" in EVALUATING_MODEL_NAME:
        return "alt_results_qwen25-32b.md"
    elif "mistral-small-2503" in EVALUATING_MODEL_NAME:
        return "alt_results_mistral-small-2503.md"
    elif "gpt-4o" in EVALUATING_MODEL_NAME:
        return "alt_results_gpt_4o.md"
    elif "grok-2" in EVALUATING_MODEL_NAME:
        return "alt_results_grok2.md"
    elif "gemini-2.0-flash" in EVALUATING_MODEL_NAME:
        return "alt_results_gemini2_flash.md"
    elif "claude-3-5-sonnet" in EVALUATING_MODEL_NAME:
        return "alt_results_claude-35-sonnet.md"


def get_evaluation_api_url():
    if "gpt-4.5" in EVALUATING_MODEL_NAME or "gpt-4o" in EVALUATING_MODEL_NAME:
        return "https://api.openai.com/v1/"
    elif "qwen-2.5-32b" in EVALUATING_MODEL_NAME:
        return "https://api.groq.com/openai/v1/"
    elif "mistral-small-2503" in EVALUATING_MODEL_NAME:
        return "https://api.mistral.ai/v1/"
    elif "grok-2" in EVALUATING_MODEL_NAME:
        return "https://api.x.ai/v1/"
    elif "gemini-2.0-flash" in EVALUATING_MODEL_NAME:
        return "https://generativelanguage.googleapis.com/v1beta/"
    elif "claude-3-5-sonnet" in EVALUATING_MODEL_NAME:
        return "https://api.anthropic.com/v1/"


def get_manual():
    if "gpt-4.5" in EVALUATING_MODEL_NAME:
        return True
    return False


EVALUATION_FOLDER = get_evaluation_folder()
TARGET_GIT_TABLE_RESULT = get_git_table_result()
EVALUATION_API_URL = get_evaluation_api_url()
MANUAL = get_manual()
