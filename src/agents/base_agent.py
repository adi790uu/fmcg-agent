from ollama import Client
from core.utils import tools
from prompts.main import get_tool_call_prompt
from core.config import MODEL
import json


class Agent:
    def __init__(self, messages):
        self.client = Client()
        self.messages = messages
        self.model = MODEL
        self.tools = tools

    def generate_response(self, result: str = None):
        system_prompt = """
            You are an agent responsible for providing appropriate answers to users,
            the answer should be based on the latest user query as well ast the result
            provided to you. Only provided relevant answer to user query.
        """  # noqa

        self.messages.extend(
            [
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"""
                        Describe this for the user in natural human language ->
                        {json.dumps(result)}
                        if None answer to the user query in a general way.
                    """,
                },
            ]
        )
        response = self.client.chat(model=self.model, messages=self.messages)
        return response["message"]["content"]

    def tool_call(self, user_query):
        self.messages.extend(
            [
                {"role": "system", "content": get_tool_call_prompt()},
                {
                    "role": "user",
                    "content": f"""Provide the most appropriate tool for the query: {user_query}""",
                },
            ]
        )
        response = self.client.chat(model=self.model, messages=self.messages)
        tool_response = response["message"]["content"]

        if tool_response == "None":
            return None, None

        if "<tool>" in tool_response and "</tool>" in tool_response:
            tool_start = tool_response.index("<tool>") + 6
            tool_end = tool_response.index("</tool>")
            tool_name = tool_response[tool_start:tool_end]
            args_start = tool_response.index("<arguments>") + 11
            args_end = tool_response.index("</arguments>")
            args_str = tool_response[args_start:args_end]

            return tool_name, args_str

    def explain_result(self, tool_result):
        messages = [
            {"role": "system", "content": self.get_system_prompt()},
            {
                "role": "user",
                "content": f"""
                    Please explain this result: {json.dumps(tool_result)}
                """,
            },
        ]
        return self.generate_response(messages)
