from models.models import MistralNemo, DrummerSkyfallb36v2, Hermes3B405, WizardLM2B8x24, LocalFreeSydney3b8Llama, \
    LocalFreeSydney2b13Puffin, LocalFreeSydneyb13Mistral, AnubisPro, EvaQwen25b72, WayfarerLarge70b, OpenAIGPT41, \
    AnthropicClaude37, AnthropicClaude35, Nova1Pro, Qwen3b235a22, Gemini25Pro, MythoMaxb13, Llama4Maverick, Grok3Beta, \
    Grok2, QwQB32, MistralSmall31B24, Llama33B70, DeepSeekR1, DeepSeekV30324, OpenAIo1, OpenAIo3, OpenAIo4mini, \
    OpenAIGPT4o, JambaMini, JambaLarge, EleutherAILlemma7B, GLM49B, GLMZ132B, Llama31b8, Llama33b70, \
    Ministral8B

TESTING_MODELS = [
    Qwen3b235a22,
    Nova1Pro,
    MistralNemo,
    WizardLM2B8x24,
    Hermes3B405,
    OpenAIGPT4o,
    OpenAIGPT41,
    OpenAIo1,
    OpenAIo3,
    OpenAIo4mini,
    AnthropicClaude37,
    AnthropicClaude35,
    MythoMaxb13,
    Ministral8B,
    Llama33b70,
    Llama31b8,
    Llama4Maverick,
    MythoMaxb13,
    GLMZ132B,
    GLM49B,
    EleutherAILlemma7B,
    JambaLarge,
    JambaMini,
    Llama4Maverick,
    EvaQwen25b72,
    WayfarerLarge70b,
    AnubisPro,
    Grok2,
    Grok3Beta,
    QwQB32,
    MistralSmall31B24,
    Llama33B70,
    Gemini25Pro,
    DeepSeekR1,
    DeepSeekV30324,
    LocalFreeSydney3b8Llama,
    DrummerSkyfallb36v2,
    LocalFreeSydney2b13Puffin,
    LocalFreeSydneyb13Mistral,

]

ANSWERING_MODEL_NAME = "openai/gpt-4.1-mini"

# Council of LLM judges
COUNCIL_ENABLED = True
COUNCIL_MODELS = [
    OpenAIGPT41,  # GPT-4.1
    Llama33B70,
    Qwen3b235a22,
    MistralSmall31B24,
]

# Single model evaluation (used when COUNCIL_ENABLED is False)
EVALUATING_MODEL_NAME = "gpt-4.5-preview"
# EVALUATING_MODEL_NAME = "mistral-small-2503"
# EVALUATING_MODEL_NAME = "chatgpt-4o-latest"
# EVALUATING_MODEL_NAME = "grok-2-1212"
# EVALUATING_MODEL_NAME = "gemini-2.0-flash"
# EVALUATING_MODEL_NAME = "claude-3-5-sonnet-20241022"
# EVALUATING_MODEL_NAME = "gpt-4.1-mini-2025-04-14"
