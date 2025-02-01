from typing import List
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage


class InMemoryHistory(BaseChatMessageHistory):
    """In memory implementation of chat message history from Langchain."""

    messages: List[BaseMessage] = []

    def add_messages(self, messages: List[BaseMessage]) -> None:
        """Add a list of messages to the store"""
        self.messages.extend(messages)

    def clear(self) -> None:
        self.messages = []