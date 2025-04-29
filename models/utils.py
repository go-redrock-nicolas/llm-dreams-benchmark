from enum import Enum
from typing import TypedDict


class Provider(Enum):
    OPENAI = "openai"
    OPENROUTER = "openrouter"
    OLLAMA = "ollama"
    ANTHROPIC = "anthropic"


class MessageTuple(TypedDict):
    role: str
    content: str
