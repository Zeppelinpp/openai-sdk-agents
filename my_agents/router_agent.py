import os
from agents import Agent, OpenAIChatCompletionsModel, Tool


class RouterAgent(Agent):
    def __init__(self, openai_client, tools: list[Tool], **kwargs):
        self.name = "Orchestration Agent"
        self.instructions = f"""
        You are the orchestration agent and decision maker for a certain task. You can use the tools given to you to get tasks done.
        You should decide wether or not use the tools and you can call the relevant tools in order.
        Always review the results before making a decision. When the context is enough, output the final answer.
        """
        self.model = OpenAIChatCompletionsModel(
            model="deepseek-chat",
            openai_client=openai_client,
        )
        super().__init__(name=self.name, instructions=self.instructions, model=self.model, tools=tools, **kwargs)
