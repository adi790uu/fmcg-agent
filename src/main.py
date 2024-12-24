import streamlit as st
import json
from agents.base_agent import Agent
from services.product_service import ProductService
from services.order_service import OrderService
import asyncio


product_service = ProductService()
order_service = OrderService()


async def execute_tool(tool_name, arguments):
    if tool_name == "get_all_products_info":
        return await product_service.get_all_products_info()
    elif tool_name == "get_product_info":
        return await product_service.get_product_info(arguments)
    elif tool_name == "get_product_stock":
        return await product_service.get_product_stock(arguments)
    elif tool_name == "add_products_to_cart":
        return await order_service.add_products_to_cart(arguments)
    elif tool_name == "remove_products_from_cart":
        return await order_service.remove_products_from_cart(arguments)
    elif tool_name == "create_order":
        return await order_service.create_order()
    elif tool_name == "get_current_total":
        return await order_service.get_current_total()
    elif tool_name == "cancel_order":
        return await order_service.cancel_order(arguments)
    elif tool_name == "get_current_cart_items":
        return await order_service.get_current_cart_items()
    elif tool_name == "get_all_orders":
        return await order_service.get_all_orders()
    return {"error": "Unknown tool"}


async def chat_with_tools(prompt, messages: list[dict]):
    agent = Agent(messages.copy())
    tool_calls = agent.tool_call(user_query=prompt)
    tool_results = []
    for tool_call in tool_calls:
        result = json.dumps(
            await execute_tool(tool_call["tool_name"], tool_call["arguments"])
        )
        tool_results.append(result)
    return agent.generate_response(json.dumps(tool_results))


async def main():

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

        result = await chat_with_tools(
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
    asyncio.run(main())
