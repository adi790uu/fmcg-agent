import re


def parse_tool_response(tool_response):
    if tool_response.strip() == "<tool_call>None</tool_call>":
        return []

    tool_calls = []
    pattern = r"<tool>(.*?)</tool><arguments>(.*?)</arguments>"
    matches = re.findall(pattern, tool_response)

    for match in matches:
        tool_calls.append(
            {
                "tool_name": match[0],
                "arguments": match[1],
            }
        )
    return tool_calls
