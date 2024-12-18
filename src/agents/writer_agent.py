import json
from base_agent import Agent
from core.config import MODEL


class WriterAgent(Agent):
    def __init__(self):
        super().__init__(
            purpose="natural_language_generation",
            model=MODEL,
        )

    def get_system_prompt(self, explain=True):
        sys_v1 = """
            You are an assistant that explains technical information in a natural,
            conversational way. Convert the given data into a helpful, easy-to-understand response.
        """  # noqa

        sys_v2 = """
            You are an assistant who is very good in responding to general
            user query, just respond to the user message in a quirky way.
        """  # noqa

        if explain:
            return sys_v1

        return sys_v2

    def respond(self, prompt: str):
        messages = [
            {
                "role": "system",
                "content": self.get_system_prompt(explain=False),
            },
            {
                "role": "user",
                "content": f"{prompt}",
            },
        ]
        return self.generate_response(messages)
