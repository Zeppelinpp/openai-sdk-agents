import asyncio, os
from agents import (
    AsyncOpenAI,
    Runner,
    MessageOutputItem,
    ItemHelpers,
    set_default_openai_client,
    set_tracing_disabled,
)
from tools.web_search import web_reader
from my_agents.web_agent import WebAgent
from my_agents.router_agent import RouterAgent
from hooks.myhooks import CustomAgentHooks

openai_client = AsyncOpenAI(
    base_url="https://api.deepseek.com",
    api_key=os.getenv("DS_KEY"),
)
set_default_openai_client(openai_client, use_for_tracing=False)
set_tracing_disabled(disabled=True)

web_agent = WebAgent(openai_client=openai_client).as_tool(
    tool_name="web_search_agent",
    tool_description="Search the web to get urls leading to relevant information",
)

router_agent = RouterAgent(openai_client=openai_client, tools=[web_agent, web_reader])


async def main(msg):
    hooks = CustomAgentHooks(display_name="Orchestration")
    result = await Runner.run(router_agent, msg, hooks=hooks)

    for item in result.new_items:
        if isinstance(item, MessageOutputItem):
            text = ItemHelpers.text_message_output(item)
            if text:
                print(f"Running step: {text}")
    print(f"Final answer: {result.final_output}")


if __name__ == "__main__":
    asyncio.run(main("I want detailed news of CNN and fox today. Give me link to checkout further information."))
