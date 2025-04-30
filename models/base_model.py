import re
import os
from enum import Enum
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Union, Dict, Any, Sequence, Literal, Callable, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, FunctionMessage, AIMessage
from langchain_core.tools import BaseTool, StructuredTool, tool
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_anthropic import ChatAnthropic
from openai import OpenAI, NOT_GIVEN
from openai.types import Completion
from openai.types.chat import ChatCompletion

from models.utils import Provider, ChatMessage, ApiError, RefusalError


# noinspection StrFormat
class BaseModel:
    model: str = ""
    pretty_name: str = ""
    temperature = 0.0
    num_predict = 0
    num_ctx = 0
    provider = ""
    format = None
    top_p = None
    top_k = None
    reasoning = False
    base_prompt = "{system_prompt}"
    system_prompt = None
    _default_system_prompt = "You are a helpful assistant."
    prompt_template = "{prompt}"

    def __init__(self, system_prompt: str = None):

        if self.provider == Provider.OPENAI:
            self.llm = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY"),

            )
        elif self.provider == Provider.OPENROUTER:
            self.llm = OpenAI(
                api_key=os.getenv("OPENROUTER_API_KEY"),
                base_url="https://openrouter.ai/api/v1",
                max_retries=3,

            )
        elif self.provider == Provider.OLLAMA:
            self.llm = OpenAI(
                base_url='http://localhost:11434/v1',
                api_key='ollama',  # required, but unused
                max_retries=3,

            )
        elif self.provider == Provider.ANTHROPIC:
            self.llm = OpenAI(
                api_key=os.getenv("ANTHROPIC_API_KEY"),
                base_url="https://api.anthropic.com/v1/",
                max_retries=3,

            )
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

        if system_prompt is None and self.system_prompt is None:
            system_prompt = self._default_system_prompt
        elif self.system_prompt is not None:
            system_prompt = self.system_prompt

        self.setup_system_prompt(system_prompt)

    def prepend_system_prompt(self, messages):
        """
        Prepend the global system prompt to the list of messages.
        """
        return [
            SystemMessage(content=self.system_prompt)
        ] + messages

    @staticmethod
    def strip_thinking_tokens(text: str) -> str:
        """
        Remove all tokens enclosed in <think> and </think> from the text.
        This function uses a regular expression with DOTALL to ensure multi-line thinking is removed.
        """
        pattern = re.compile(r"(?s)<think>(.*?)</think>")
        cleaned = pattern.sub("", text)
        return cleaned.strip()

    def format_prompt(self, prompt):
        return self.prompt_template.replace("{prompt}", prompt)

    @staticmethod
    def _is_string_message(message):
        return isinstance(message, str)

    @staticmethod
    def _is_base_message(message):
        return isinstance(message, BaseMessage)

    @staticmethod
    def _is_list_of_messages(message):
        return isinstance(message, list)

    def _estimate_tokens(self, messages: List[Union[ChatMessage, dict[str, str]]]) -> int:
        """
        Estimate the number of tokens in a list of messages.
        Uses a simple approximation method.

        Args:
            messages: List of message objects

        Returns:
            int: Estimated token count
        """
        # Simple estimation based on text length
        total_text = ""
        for msg in messages:
            if isinstance(msg['content'], str):
                total_text += msg['content']
            elif isinstance(msg['content'], list):
                for part in msg['content']:
                    if isinstance(part, dict) and "text" in part:
                        total_text += part["text"]

        # Rough estimation: ~4 characters per token for English text
        return round(len(total_text) // 2)

    def _adjust_output_limit(self, messages: List[Union[ChatMessage, dict[str, str]]]) -> int:
        """
        Dynamically adjust output token limit based on input length.

        Args:
            messages: The messages to be sent to the model

        Returns:
            int: Adjusted token limit
        """
        # Only apply for large inputs (>50k tokens)
        input_tokens = self._estimate_tokens(messages)
        if input_tokens + self.num_predict < self.num_ctx:
            return self.num_predict - input_tokens

        # Get model context limits
        # Each model class can define a 'context_window' attribute with its limits
        context_window = self.num_ctx

        # Calculate available tokens, with a buffer
        buffer = round(context_window * 0.1)
        available_tokens = context_window - input_tokens - buffer
        if available_tokens < context_window + 200:
            return available_tokens - 1000

        # Use minimum of original num_predict or available tokens
        adjusted_limit = min(self.num_predict, available_tokens)

        print(f"[TokenAdjustment] Input tokens: ~{input_tokens}, Context window: {context_window}")
        print(f"[TokenAdjustment] Adjusting max output from {self.num_predict} to {adjusted_limit} tokens")

        return adjusted_limit

    def invoke(
            self,
            message_input: Union[str, dict[str, str], ChatMessage, list[ChatMessage], list[dict[str, str]]],
            strip_thinking_tokens: bool = True,
            return_as_list: bool = False,
    ) -> Union[ChatMessage, List[ChatMessage], List[dict]]:
        """
        Invoke the underlying LLM with the given message(s).

        This method wraps plain text into message objects and handles optional retries.
        For very large inputs, it dynamically adjusts the output token limit.

        Args:
            return_as_list:
            message_input:
            strip_thinking_tokens:

        Returns:
            AIMessage:

        """

        if isinstance(message_input, str):
            messages = [ChatMessage(role="user", content=message_input)]
        elif isinstance(message_input, dict):
            messages = [ChatMessage(role="user", content=message_input["content"])]
        else:
            messages = message_input

        # For large inputs, adjust token limit
        original_limit = None
        if self._estimate_tokens(messages) + self.num_predict > self.num_ctx:
            adjusted_limit = self._adjust_output_limit(messages)
            # todo fix the limit not being changed
            # Save original limit to restore later
            original_limit = self.num_predict
            self.num_predict = adjusted_limit

        # Invoke with potentially adjusted limits
        # Don't wrap if the system prompt is built into the prompt template, as it will be prepended to the messages anyway.
        # Also dont wrap if this is a list of messages and the first one is a SystemMessage
        if not self.prompt_template.__contains__("{system_prompt}") and not messages[0]['role'] == 'system' and not isinstance(
                messages, list):
            messages = self.prepend_system_prompt(messages)
        else:
            # If template contains system prompt, only keep it in the first message
            if self._is_list_of_messages(messages):
                first_message = messages[0]
                rest_messages = messages[1:]
                first_message['content'] = first_message['content'].replace("{system_prompt}", self.system_prompt)
                if "metadata" in first_message:
                    first_message.pop('metadata')
                # Process the rest of messages to replace system prompt with empty string
                processed_rest = []
                for msg in rest_messages:
                    msg['content'] = msg['content'].replace("{system_prompt}", "")
                    if "metadata" in msg:
                        msg.pop('metadata')
                    processed_rest.append(msg)

                messages = [first_message] + processed_rest

        # print(f"[ModelInvocation] Invoking model {self.model} with {len(messages)} messages")
        # print(f"[ModelInvocation] Messages: {messages}")
        result = self.llm.chat.completions.create(
            messages=messages,
            model=self.model,
            temperature=self.temperature or NOT_GIVEN,
            max_completion_tokens=self.num_predict or NOT_GIVEN,
        )

        if "error" in result.model_extra or result.choices[0].message.content is None:
            raise ApiError(f"[{result.model_extra['error']['code']}] {result.model_extra['error']['message']} {result.model_extra['error']['metadata']['raw']}")
        if result.choices[0].message.refusal:
            raise RefusalError(f"Refusal Error: {result.choices[0].message.refusal}")
        result = ChatMessage(
            role="assistant",
            content=result.choices[0].message.content,
            metadata={}
        )

        # Restore the original limit if changed
        self.num_predict = original_limit or self.num_predict
        if strip_thinking_tokens:
            result['content'] = self.strip_thinking_tokens(result['content']).strip()

        if return_as_list:
            messages.append(result)
            return messages
        else:
            return result

    def get_model_slug(self):
        return self.model.replace("hf.co/", "").replace("/", "_").replace(".", "-")

    def setup_system_prompt(self, system_prompt: str):
        self.system_prompt = self.base_prompt.replace("{system_prompt}", system_prompt)


def dump_messages_json(messages: List[BaseMessage]) -> str:
    string = ""
    for message in messages:
        string += f"{message.model_dump_json(exclude_none=True)},"

    return "[" + string + "]"
