from models.models import MistralNemo, LocalSkyfallb36, Hermes3B405, WizardLM2B8x24, LocalFreeSydney3b8Llama, \
    LocalFreeSydney2b13Puffin, LocalFreeSydneyb13Mistral, AnubisPro, EvaQwen25b72, WayfarerLarge70b

TESTING_MODELS = [
    AnubisPro,
    EvaQwen25b72,
    WayfarerLarge70b,
    LocalFreeSydney3b8Llama,
    LocalFreeSydney2b13Puffin,
    LocalFreeSydneyb13Mistral,
    WizardLM2B8x24,
    Hermes3B405,
    LocalSkyfallb36,
    MistralNemo,

]

ANSWERING_MODEL_NAME = "openai/gpt-4.1-mini"

# Council of LLM judges
COUNCIL_ENABLED = True
COUNCIL_MODELS = [
    "anthropic/claude-3.7-sonnet",  # Claude 3.7 Sonnet
    "openai/gpt-4.1",  # GPT-4.1
    "google/gemini-2.5-pro-preview-03-25"  # Gemini Pro 2.5
]

# Single model evaluation (used when COUNCIL_ENABLED is False)
EVALUATING_MODEL_NAME = "gpt-4.5-preview"
# EVALUATING_MODEL_NAME = "mistral-small-2503"
# EVALUATING_MODEL_NAME = "chatgpt-4o-latest"
# EVALUATING_MODEL_NAME = "grok-2-1212"
# EVALUATING_MODEL_NAME = "gemini-2.0-flash"
# EVALUATING_MODEL_NAME = "claude-3-5-sonnet-20241022"
# EVALUATING_MODEL_NAME = "gpt-4.1-mini-2025-04-14"
