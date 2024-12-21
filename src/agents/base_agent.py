from ollama import Client
from core.utils import parse_tool_response
from core.config import tools
from prompts.main import get_tool_call_prompt, get_agent_prompt
from core.config import MODEL
import json


class Agent:
    def __init__(self, messages):
        self.client = Client()
        self.messages = messages
        self.model = MODEL
        self.tools = tools
        self.prompt = get_agent_prompt()

        if not any(
            msg["role"] == "system" and msg["content"] == self.prompt
            for msg in self.messages
        ):
            self.messages.append({"role": "system", "content": self.prompt})

    def generate_response(self, result: str = None):

        self.messages.extend(
            [
                {
                    "role": "user",
                    "content": f"""
                        user_query: {self.messages[-1]}
                        Result: {json.dumps(result)}

                        - Answer the user query with reference to the result
                        provided to you.
                    """,
                },
            ]
        )
        response = self.client.chat(model=self.model, messages=self.messages)
        return response["message"]["content"]

    def tool_call(self, user_query):
        message_for_tool_call = [
            {
                "role": "system",
                "content": get_tool_call_prompt(),
            },
            {
                "role": "user",
                "content": f"""Provide the most appropriate tools for the
                        query: {user_query}""",
            },
        ]

        response = self.client.chat(
            model=self.model,
            messages=message_for_tool_call,
        )
        tool_response = response["message"]["content"]
        tool_calls = parse_tool_response(tool_response=tool_response)
        return tool_calls
