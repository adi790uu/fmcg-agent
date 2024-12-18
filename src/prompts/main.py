import json
from core.utils import tools


def get_tool_call_prompt():
    return f"""
            You are an assistant focused on using tools effectively to retrieve information.
            Available tools: {json.dumps(tools, indent=2)}

            To use a tool, respond with:
            FORMAT ->
                **<tool>tool_name</tool><arguments>product_name</arguments**
            Example ->
            1. <tool>get_product_info</tool><arguments>Personal Care</arguments>
            2. <tool>get_stock_status</tool><arguments>Hair Oil</arguments>

            IMPORTANT ->
            - **Always close the tags -> <tool></tool>, <arguments></arguments>**
            - **Only respond with the tool call, no other text**
            - **If the query by the user does not require a tool call, return None**
        """  # noqa
