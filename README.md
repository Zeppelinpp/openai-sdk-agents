# OpenAI SDK Agents

A collection of agent implementations built with the OpenAI Agent SDK, showcasing various practical applications and use cases.

## Overview

This project explores how to build custom agents using the OpenAI Agent SDK with different LLM Providers.

## Features

- **Web Search Agent**: An agent that can search the web for real-time information using the SerpAPI
- Extensible architecture for adding new agent types
- Custom tool implementations that can be shared across different agents
- Support for multiple LLM providers (OpenAI, DeepSeek, etc.)

Adding up ...

## Project Structure

```
openai-sdk-agents/
├── my_agents/         # Agent implementations
├── tools/             # Custom tools for agents
├── tests/             # Test cases
├── main.py            # Main entry point
```

## Requirements

- Python 3.13+
- Dependencies listed in pyproject.toml:
  - openai-agents
  - openai
  - google-search-results
  - serpapi

## Getting Started

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -e .`
5. Set up environment variables in `.env`:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `SERPAPI_KEY`: Your SerpAPI key
   - `DS_KEY`: Your DeepSeek API key (if using DeepSeek)
6. Run the example: `python main.py`

## Usage

### Web Search Agent

```python
from agents import Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled
from my_agents.web_agent import WebAgent

# Initialize the client
client = AsyncOpenAI(base_url="LLM Provider's url", api_key="your-api-key")
set_default_openai_client(ds_client, use_for_tracing=False)
set_tracing_disabled(disabled=True)
# Create a web agent
web_agent = WebAgent(client)

# Run the agent with a query
result = Runner.run_sync(web_agent, "Detailed information of CNN news today")
print(result.final_output)
```

## Extending the Project

You can extend this project by:

1. Creating new agent types in the `my_agents` directory
2. Implementing custom tools in the `tools` directory
3. Modifying the existing agents to add new capabilities

## License

MIT License
