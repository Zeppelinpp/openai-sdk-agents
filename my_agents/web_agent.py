import os
from agents import Agent, OpenAIChatCompletionsModel
from tools.web_search import web_search
from dotenv import load_dotenv

load_dotenv()
DS_KEY = os.getenv("DS_KEY")


class WebAgent(Agent):
    def __init__(self, openai_client, **kwargs):
        self.name = "Web Search Agent"
        self.instructions = """ 
        You are a web search agent.
        You will be called if certain information that is not your knowledge is needed.
        You need to use the web_search tool to search the web.
        """
        self.model = OpenAIChatCompletionsModel(
            model="deepseek-chat",
            openai_client=openai_client,
        )
        self.tools = [web_search]
        super().__init__(
            name=self.name,
            instructions=self.instructions,
            model=self.model,
            tools=self.tools,
            **kwargs,
        )
