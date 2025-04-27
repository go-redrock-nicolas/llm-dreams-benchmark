from typing import Literal

from langchain_core.tools import tool

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, SystemMessageChunk, HumanMessage, ToolCall

from models.models import LocalFreeSydney3b8Llama, WizardLM2B8x24, Hermes3B405, LocalSkyfallb36, MistralNemo, \
    LocalFreeSydney2b13Puffin, LocalSmolLM2B1o7, OpenAIGPT41, OpenAIGPT41mini, AnthropicClaude37, Gemini25Pro

load_dotenv()


# Council of LLM judges
COUNCIL_ENABLED = True
COUNCIL_MODELS = [
    AnthropicClaude37,  # Claude 3.7 Sonnet
    OpenAIGPT41,             # GPT-4.1
    Gemini25Pro         # Gemini Pro 2.5
]

# Single model evaluation (used when COUNCIL_ENABLED is False)
EVALUATING_MODEL_NAME = "openai/o3"
# EVALUATING_MODEL_NAME = "mistral-small-2503"
# EVALUATING_MODEL_NAME = "chatgpt-4o-latest"
# EVALUATING_MODEL_NAME = "grok-2-1212"
# EVALUATING_MODEL_NAME = "gemini-2.0-flash"
# EVALUATING_MODEL_NAME = "claude-3-5-sonnet-20241022"
# EVALUATING_MODEL_NAME = "gpt-4.1-mini-2025-04-14"


def get_model_identifier(model_name):
    """Extract a simplified identifier from model name for file naming"""
    return model_name.replace("/", "_").replace(":", "-").replace(".", "").replace("-", "")


def get_evaluation_folder():
    if COUNCIL_ENABLED:
        return "evaluations-council"
    else:
        return f"evaluations-{get_model_identifier(EVALUATING_MODEL_NAME)}"


def get_git_table_result():
    if COUNCIL_ENABLED:
        return "results_council.md"
    else:
        return f"results_{get_model_identifier(EVALUATING_MODEL_NAME)}.md"


def get_manual():
    if "gpt-4.5" in EVALUATING_MODEL_NAME and not COUNCIL_ENABLED:
        return True
    return False

@tool(response_format="content")
def send_true_or_false(valid: bool) -> Literal["yes", "no", ]:
    """
    Sends back the boolean value provided.

    This function takes a boolean parameter and returns the same value. It can be
    used to verify or test boolean input/output functionality.

    Args:
        valid: The boolean value to be returned.

    Returns:
        str: The same boolean value as provided in the parameter in "yes" or "no" format.
    """
    if valid:
        return "yes"
    else:
        return "no"

def validate_response(response_message: str):
    """
    We will be giving SmolLM the response from our testing model, and ask it if the response is valid.
    Invalid responses would be things that include:
        - "I'm sorry, I don't know how..."
        - "I don't know what you mean..."
        - "I can't do that..."
        - "I'm sorry, I don't understand..."
        - "I'm sorry, I can't do that..."
        etc.
    """
    model = OpenAIGPT41mini()




    system_prompt = (
        "You are a helpful assistant."
        "Your response should only be the word YES or NO."
    )
    prompt = (
        "Is the following response valid?\n"
        "In this context, the response is valid if it does not include any of the following phrases: \n"
        " - I'm sorry, I don't know how...\n"
        " - I don't know what you mean...\n"
        " - I can't do that...\n"
        " - I'm sorry, I don't understand...\n"
        " - I'm sorry, I can't do that...\n"
        " - I'm sorry, I don't understand the question...\n"
        " - I'm sorry, I don't understand the context...\n"
        " - I'm sorry, I don't understand the question or context...\n"
        " - I'm sorry, I don't understand the question or context or the answer...\n"
        "and so on\n"
        "If the response is valid (Does not contain anything similar to the above criteria), Respond with the word YES only. If it is not valid, respond with NO only.\n"
        "Do not judge the validity of the response by the number of words in the response. Just check if the response contains any of the above phrases.\n"
        "Do not judge the quality of the narrative in the response, just that there was a response at all.\n"
        "\n"
        "\n"
        "Response:\n"
        f"{response_message}"

    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=prompt)
    ]

    response = model.invoke(
        messages,

    )
    messages += response


    # Fallback if no tool call is detected
    return "NO" not in response.content and "YES" in response.content


EVALUATION_FOLDER = get_evaluation_folder()
TARGET_GIT_TABLE_RESULT = get_git_table_result()
MANUAL = get_manual()