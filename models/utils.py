from enum import Enum
from typing import TypedDict, Literal, Union


class Provider(Enum):
    OPENAI = "openai"
    OPENROUTER = "openrouter"
    OLLAMA = "ollama"
    ANTHROPIC = "anthropic"


class ChatMessage(TypedDict):
    role: str
    content: str
    metadata: Union[dict, None]


def system_message(content: str) -> ChatMessage:
    return ChatMessage(
        role="system",
        content=content,
        metadata=None,

    )


def human_message(content: str) -> ChatMessage:
    return ChatMessage(
        role="user",
        content=content,
        metadata=None,

    )


def ai_message(content: str, metadata: dict = None) -> ChatMessage:
    return ChatMessage(
        role="assistant",
        content=content,
        metadata=metadata,

    )

class ModelError(Exception):
    pass

class UnknownError(Exception):
    pass

class RefusalError(Exception):
    refusal_reason: str
    def __init__(self, refusal_reason: str, *args: object):
        self.refusal_reason = refusal_reason
        super().__init__(*args)


class ApiError(Exception):
    pass