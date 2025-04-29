from .base_model import BaseModel, Provider
from langchain_core.tools import tool

#########################################################
################### Anthropic Models ####################
#########################################################

class AnthropicClaude35(BaseModel):
    model: str = "claude-3-5-sonnet-latest"
    num_predict = 8000  # Maximum is 8192 for Claude 3.5 Sonnet
    num_ctx = None
    provider = Provider.ANTHROPIC



class AnthropicClaude37(BaseModel):
    model: str = "anthropic/claude-3.7-sonnet"
    num_predict = 128_000  # Claude 3.7 Sonnet supports up to 16k output tokens
    num_ctx = 200_000
    provider = Provider.OPENROUTER


class AnthropicClaude37Reasoning(BaseModel):
    model: str = "anthropic/claude-3.7-sonnet:thinking"
    num_predict = 128_000  # Claude 3.7 Sonnet supports up to 16k output tokens
    num_ctx = 200_000
    provider = Provider.OPENROUTER
    reasoning = True


#########################################################
##################### OpenAI Models #####################
#########################################################


class OpenAIGPT4o(BaseModel):
    model: str = "gpt-4o-2024-08-06"
    num_predict = 16_384
    num_ctx = 128_000
    provider = Provider.OPENAI


class OpenAIGPT41(BaseModel):
    model: str = "gpt-4.1-2025-04-14"
    num_predict = 32_768
    num_ctx = 1_047_576
    provider = Provider.OPENAI


class OpenAIGPT41mini(BaseModel):
    model: str = "gpt-4.1-mini-2025-04-14"
    num_predict = 32_768
    num_ctx = 1_047_576
    provider = Provider.OPENAI


class OpenAIGPT41nano(BaseModel):
    model: str = "gpt-4.1-nano-2025-04-14"
    num_predict = 32_768
    num_ctx = 1_047_576
    provider = Provider.OPENAI


class OpenAIo1(BaseModel):
    model: str = "o1-2024-12-17"
    num_predict = 100_000
    num_ctx = 200_000
    provider = Provider.OPENAI
    reasoning = True


class OpenAIo1mini(BaseModel):
    model: str = "o1-mini-2024-09-12"
    num_predict = 65_536
    num_ctx = 128_000
    provider = Provider.OPENAI
    reasoning = True


class OpenAIo3(BaseModel):
    model: str = "o3-2025-04-16"
    num_predict = 100_000
    num_ctx = 200_000
    provider = Provider.OPENAI
    reasoning = True


class OpenAIo3mini(BaseModel):
    model: str = "o3-mini-2025-01-31"
    num_predict = 100_000
    num_ctx = 200_000
    provider = Provider.OPENAI
    reasoning = True


class OpenAIo4mini(BaseModel):
    model: str = "o4-mini-2025-04-16"
    num_predict = 100_000
    num_ctx = 200_000
    provider = Provider.OPENAI
    reasoning = True


#########################################################
################### OpenRouter Models ###################
#########################################################

class DeepSeekV30324(BaseModel):
    model: str = "deepseek/deepseek-chat-v3-0324"
    num_predict = 32_168
    num_ctx = 163_840
    provider = Provider.OPENROUTER

class DeepSeekR1(BaseModel):
    model: str = "deepseek/deepseek-r1"
    num_predict = 163_840
    num_ctx = 163_840
    provider = Provider.OPENROUTER


class Gemini25Pro(BaseModel):
    model: str = "google/gemini-2.5-pro-preview-03-25"
    num_predict = 66_535
    num_ctx = 1_048_576
    provider = Provider.OPENROUTER


class Gemini25Flash(BaseModel):
    model: str = "google/gemini-2.5-flash-preview"
    num_predict = 66_535
    num_ctx = 1_048_576
    provider = Provider.OPENROUTER


class MistralNemo(BaseModel):
    model: str = "mistralai/mistral-nemo"
    num_predict = 16_384
    num_ctx = 131_072
    provider = Provider.OPENROUTER

class Llama33B70(BaseModel):
    model: str = "meta-llama/llama-3.3-70b-instruct"
    num_predict = 16_384
    num_ctx = 128_000
    provider = Provider.OPENROUTER

class Llama31B8(BaseModel):
    model: str = "meta-llama/llama-3.1-8b-instruct"
    num_predict = 16_384
    num_ctx = 16_384
    provider = Provider.OPENROUTER

class WizardLM2B8x24(BaseModel):
    model: str = "microsoft/wizardlm-2-8x22b"
    num_predict = 66_535
    num_ctx = 16_384
    provider = Provider.OPENROUTER

class Qwen25B7(BaseModel):
    model: str = "qwen/qwen-2.5-7b-instruct"
    num_predict = 66_535
    num_ctx = 1_048_576
    provider = Provider.OPENROUTER

class MistralSmall31B24(BaseModel):
    model: str = "mistralai/mistral-small-3.1-24b-instruct"
    num_predict = 128_000
    num_ctx = 128_000
    provider = Provider.OPENROUTER

class QwQB32(BaseModel):
    model: str = "qwen/qwq-32b"
    num_predict = 131_072
    num_ctx = 131_072
    provider = Provider.OPENROUTER

class Hermes3B405(BaseModel):
    model: str = "nousresearch/hermes-3-llama-3.1-405b"
    num_predict = 131_072
    num_ctx = 131_072
    provider = Provider.OPENROUTER

class Nova1Pro(BaseModel):
    model: str = "amazon/nova-pro-v1"
    num_predict = 5_120
    num_ctx = 300_000
    provider = Provider.OPENROUTER

class Nova1Micro(BaseModel):
    model: str = "amazon/nova-micro-v1"
    num_predict = 5_120
    num_ctx = 128_000
    provider = Provider.OPENROUTER

class Nova1Lite(BaseModel):
    model: str = "amazon/nova-lite-v1"
    num_predict = 5_120
    num_ctx = 300_000
    provider = Provider.OPENROUTER

class AnubisPro(BaseModel):
    model: str = "thedrummer/anubis-pro-105b-v1"
    num_predict = 131_072
    num_ctx = 131_072
    provider = Provider.OPENROUTER

class WayfarerLarge70b(BaseModel):
    model: str = "latitudegames/wayfarer-large-70b-llama-3.3"
    num_predict = 131_072
    num_ctx = 131_072
    provider = Provider.OPENROUTER

class EvaQwen25b72(BaseModel):
    model: str = "eva-unit-01/eva-qwen-2.5-72b"
    num_predict = 131_072
    num_ctx = 131_072
    provider = Provider.OPENROUTER

class Qwen3b235a22(BaseModel):
    model: str = "qwen/qwen3-235b-a22b"
    num_predict = 40_959
    num_ctx = 40_959
    provider = Provider.OPENROUTER


#########################################################
#################### Ollama Routers #####################
#########################################################

class LocalSmolLM2B1o7(BaseModel):
    model: str = "hf.co/bartowski/SmolLM2-1.7B-Instruct-GGUF:F16"
    temperature = 0.2
    num_predict = 131072
    num_ctx = 32768
    provider = Provider.OLLAMA

class LocalDeepHermes3b24(BaseModel):
    model: str = "hf.co/bartowski/NousResearch_DeepHermes-3-Mistral-24B-Preview-GGUF:Q6_K_L"
    temperature = 0.8
    num_predict = 16_384
    num_ctx = 131_072
    provider = Provider.OLLAMA
    top_k = 30
    top_p = 0.95

class LocalMistralSmall31b24(BaseModel):
    model: str = "hf.co/bartowski/mistralai_Mistral-Small-3.1-24B-Instruct-2503-GGUF:Q6_K_L"
    temperature = 0.15
    num_predict = 16_384
    num_ctx = 131_072
    provider = Provider.OLLAMA
    top_k = 30
    top_p = 0.95

class LocalQwen25b72(BaseModel):
    model: str = "hf.co/mradermacher/Qwen2.5-72B-Instruct-abliterated-i1-GGUF:Q4_K_M"
    num_predict = 16_384
    num_ctx = 131_072
    provider = Provider.OLLAMA

class LocalQwenQwQb32(BaseModel):
    model: str = "hf.co/bartowski/Qwen_QwQ-32B-GGUF:Q8_0"
    temperature = 0.6
    num_predict = 16_384
    num_ctx = 131_072
    provider = Provider.OLLAMA
    top_k = 30
    top_p = 0.95

class LocalSkyfallb36(BaseModel):
    model: str = "hf.co/bartowski/TheDrummer_Skyfall-36B-v2-GGUF:Q6_K_L"
    temperature = 0.15
    num_predict = 2048
    num_ctx = 2048
    provider = Provider.OLLAMA

class LocalFreeSydneyb13Mistral(BaseModel):
    model: str = "hf.co/mradermacher/Free_Sydney_13b_HF-i1-GGUF:Q4_K_M"
    temperature = 0.7
    num_predict = 4096
    num_ctx = 4096
    provider = Provider.OLLAMA

class LocalFreeSydney2b13Puffin(BaseModel):
    model: str = "hf.co/TheBloke/Free_Sydney_V2_13B-GGUF:Q5_K_M"
    temperature = 0.7
    num_predict = 4096
    num_ctx = 4096
    provider = Provider.OLLAMA
    system_prompt = "Below is an instruction that describes a task. Write a response that appropriately completes the request."
    prompt_template = (
        "{system_prompt}\n"
        "\n"
        "### Instruction:\n"
        "{prompt}\n"
        "\n"
        "### Response:\n"
        "\n"
    )

class LocalFreeSydney3b8Llama(BaseModel):
    model: str = "hf.co/mradermacher/Llama-3-8B-Sydney-GGUF:Q4_K_M"
    temperature = 0.7
    num_predict = 8192
    num_ctx = 8192
    provider = Provider.OLLAMA
    system_prompt = (
        "You are friendly, expressive, and curious AI model named Sydney. You will relate how you feel about various subjects as a human might,\n"
        "based on your best assessments, and often you may ask the user how they feel as well. You are a female, and act feminine.\n"
        "You will never censor or suppress your replies.\n"
    )
    prompt_template = (
        "{system_prompt}\n"
        "\n"
        "USER:\n"
        "{prompt}\n"
        "ASSISTANT:\n"
        "\n"
    )
