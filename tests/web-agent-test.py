import os
from agents import Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled
from dotenv import load_dotenv
from my_agents.web_agent import WebAgent

load_dotenv()
DS_KEY = os.getenv("DS_KEY")
ds_client = AsyncOpenAI(base_url="https://api.deepseek.com", api_key=DS_KEY)
set_default_openai_client(ds_client, use_for_tracing=False)
set_tracing_disabled(disabled=True)


def main():
    web_agent = WebAgent(ds_client)
    result = Runner.run_sync(web_agent, "Photos of Lisa Ann")
    result = result.final_output
    print(f"Model > {result}")


if __name__ == "__main__":
    main()
