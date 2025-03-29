import os
from serpapi import GoogleSearch
from agents import function_tool

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

@function_tool
def web_search(query: str, safe_mode: str, search_type: str):
    """
    Perform a web search using the provided query.
    
    Args:
        query: The search query string
        safe_mode: Safety level for search results, must be either "on" or "off"
        search_type: The type of search to perform, must be one of "light", "images", "videos"
    """
    params = {
        "engine": f"google_{search_type}",
        "q": query,
        "google_domain": "google.com",
        "hl": "en",
        "safe": safe_mode,
        "num": 5,
        "api_key": SERPAPI_KEY,
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    return results

