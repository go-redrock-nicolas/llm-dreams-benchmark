import re
import os
from enum import Enum
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Union, Dict, Any
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, FunctionMessage, AIMessage
from langchain_core.tools import BaseTool, StructuredTool, tool
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_anthropic import ChatAnthropic


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
            self.llm = ChatOpenAI(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.num_predict,  # ChatOpenAI uses 'max_tokens' instead of 'num_predict'
                api_key=os.getenv("OPENAI_API_KEY"),

            )
        elif self.provider == Provider.OPENROUTER:
            self.llm = ChatOpenAI(
                model=self.model,
                temperature=self.temperature,
                base_url="https://openrouter.ai/v1",
                api_key=os.getenv("OPENROUTER_API_KEY")
            )
        elif self.provider == Provider.OLLAMA:
            self.llm = ChatOllama(
                model=self.model,
                temperature=self.temperature,
                num_predict=self.num_predict,
                num_ctx=self.num_ctx,
                format=self.format,
                top_p=self.top_p,
                top_k=self.top_k,
            )
        elif self.provider == Provider.ANTHROPIC:
            # noinspection PyArgumentList
            self.llm = ChatAnthropic(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.num_predict,
                api_key=os.getenv("ANTHROPIC_API_KEY"),
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

    def _wrap_message(
            self,
            message_input: Union[str, BaseMessage, List[Union[str, BaseMessage]]]

    ) -> List[BaseMessage]:
        """
        Convert message_input into a list of BaseMessage objects.

        If a plain string is provided, it is wrapped into a HumanMessage.

        Args:
            message_input (Union[str, BaseMessage, List[Union[str, BaseMessage]]]):
                The input message(s) to send.

        Returns:
            List[BaseMessage]: A list of message objects.
        """


        if self._is_string_message(message_input):
            return [HumanMessage(content=self.format_prompt(message_input))]
        elif self._is_base_message(message_input):
            message_input.content = self.format_prompt(message_input.content)
            return [message_input]
        elif self._is_list_of_messages(message_input):
            messages = []
            for m in message_input:
                if self._is_string_message(m):
                    messages.append(HumanMessage(content=self.format_prompt(m)))
                elif isinstance(m, HumanMessage):
                    m.content = self.format_prompt(m.content)
                    messages.append(m)
                elif not isinstance(m, SystemMessage) and not isinstance(m, FunctionMessage) and not isinstance(m, AIMessage):
                    raise ValueError("List items must be either str or BaseMessage")
            return messages
        else:
            raise ValueError("message_input must be a str, BaseMessage, or list of these types")

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

    def _estimate_tokens(self, messages: List[BaseMessage]) -> int:
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
            if isinstance(msg.content, str):
                total_text += msg.content
            elif isinstance(msg.content, list):
                for part in msg.content:
                    if isinstance(part, dict) and "text" in part:
                        total_text += part["text"]

        # Rough estimation: ~4 characters per token for English text
        return len(total_text) // 4

    def _adjust_output_limit(self, messages: List[BaseMessage]) -> int:
        """
        Dynamically adjust output token limit based on input length.

        Args:
            messages: The messages to be sent to the model

        Returns:
            int: Adjusted token limit
        """
        # Only apply for large inputs (>50k tokens)
        input_tokens = self._estimate_tokens(messages)
        if input_tokens < 50_000:
            return self.num_predict

        # Get model context limits
        # Each model class can define a 'context_window' attribute with its limits
        context_window = getattr(self, "context_window", 0)

        # If not defined in the model class, use conservative defaults
        if context_window == 0:
            if self.provider == "openai":
                context_window = 128_000  # For newer models
            elif self.provider == "anthropic":
                context_window = 200_000  # For Claude 3 models
            elif self.provider == "ollama":
                context_window = 43_690  # Conservative default
            else:
                context_window = 32_768  # Very conservative default

        # Calculate available tokens, with 5000 token buffer
        buffer = 5000
        available_tokens = max(1000, context_window - input_tokens - buffer)

        # Use minimum of original num_predict or available tokens
        adjusted_limit = min(self.num_predict, available_tokens)

        print(f"[TokenAdjustment] Input tokens: ~{input_tokens}, Context window: {context_window}")
        print(f"[TokenAdjustment] Adjusting max output from {self.num_predict} to {adjusted_limit} tokens")

        return adjusted_limit

    def invoke(
            self,
            message_input: Union[str, BaseMessage, List[Union[str, BaseMessage]]],
            strip_thinking_tokens: bool = True,
            return_as_list: bool = False,
    ) -> Union[AIMessage, BaseMessage, List[BaseMessage]]:
        """
        Invoke the underlying LLM with the given message(s).

        This method wraps plain text into message objects and handles optional retries.
        For very large inputs, it dynamically adjusts the output token limit.

        Args:
            message_input:
            strip_thinking_tokens:

        Returns:
            AIMessage:

        """

        messages = self._wrap_message(message_input)

        # For large inputs, adjust token limit
        original_limit = None
        if self._estimate_tokens(messages) > 50_000:
            adjusted_limit = self._adjust_output_limit(messages)

            # Save original limit to restore later
            if self.provider == "openai":
                original_limit = self.llm.max_tokens
                self.llm.max_tokens = adjusted_limit
            elif self.provider == "anthropic":
                original_limit = self.llm.max_tokens
                self.llm.max_tokens = adjusted_limit
            elif self.provider == "ollama":
                original_limit = self.llm.num_predict
                self.llm.num_predict = adjusted_limit

        # Invoke with potentially adjusted limits
        # Don't wrap if the system prompt is built into the prompt template, as it will be prepended to the messages anyway.
        # Also dont wrap if this is a list of messages and the first one is a SystemMessage
        if not self.prompt_template.__contains__("{system_prompt}") and not isinstance(messages[0], SystemMessage) and not isinstance(messages, list):
            messages = self.prepend_system_prompt(messages)
        else:
            # If template contains system prompt, only keep it in the first message
            if self._is_list_of_messages(messages):
                first_message = messages[0]
                rest_messages = messages[1:]
                first_message.content = first_message.content.replace("{system_prompt}", self.system_prompt)
                # Process the rest of messages to replace system prompt with empty string
                processed_rest = []
                for msg in rest_messages:
                    if isinstance(msg, HumanMessage):
                        msg.content = msg.content.replace("{system_prompt}", "")
                    processed_rest.append(msg)

                messages = [first_message] + processed_rest

        #print(f"[ModelInvocation] Invoking model {self.model} with {len(messages)} messages")
        #print(f"[ModelInvocation] Messages: {messages}")
        result = self.llm.invoke(messages)

        # Restore the original limit if changed
        if original_limit is not None:
            if self.provider == "openai":
                self.llm.max_tokens = original_limit
            elif self.provider == "anthropic":
                self.llm.max_tokens = original_limit
            elif self.provider == "ollama":
                self.llm.num_predict = original_limit
        if strip_thinking_tokens:
            result.content = self.strip_thinking_tokens(result.content).strip()

        if return_as_list:
            messages.append(result)
            return messages
        else:
            return result
    def get_model_slug(self):
        return self.model.replace("hf.co/", "").replace("/", "_").replace(".", "-")

    def setup_system_prompt(self, system_prompt: str):
        self.system_prompt = self.base_prompt.replace("{system_prompt}", system_prompt)

class Provider(Enum):
    OPENAI = "openai"
    OPENROUTER = "openrouter"
    OLLAMA = "ollama"
    ANTHROPIC = "anthropic"

def dump_messages_json(messages: List[BaseMessage]) -> str:
    string = ""
    for message in messages:
        string += f"{message.model_dump_json(exclude_none=True)},"

    return "[" + string + "]"