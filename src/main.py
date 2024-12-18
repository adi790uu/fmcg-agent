import streamlit as st
import json
from tools.main import get_product_info, get_stock_status
from agents.base_agent import Agent


def execute_tool(tool_name, arguments):
    if tool_name == "get_product_info":
        if isinstance(arguments, str):
            arguments = {"category": arguments}
        return get_product_info(**arguments)
    elif tool_name == "get_stock_status":
        if isinstance(arguments, str):
            arguments = {"product_name": arguments}
        return get_stock_status(**arguments)
    return {"error": "Unknown tool"}


def chat_with_tools(prompt, messages: list[dict]):
    agent = Agent(messages)
    tool_name, args_str = agent.tool_call(user_query=prompt)
    result = None
    if tool_name and args_str:
        result = json.dumps(execute_tool(tool_name, args_str))

    return agent.generate_response(result)


def main():

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hey, How can I help you today!",
            }
        ]

    st.header("Chat")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Say something"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        message = st.chat_message("user")
        message.write(prompt)

        result = chat_with_tools(
            prompt=prompt,
            messages=st.session_state.messages,
        )
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result,
            }
        )

        st.rerun()


if __name__ == "__main__":
    main()
