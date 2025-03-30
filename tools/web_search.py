import os
from serpapi import GoogleSearch
from agents import function_tool
import requests
from selectolax.parser import HTMLParser

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
    results = search.get_dict()["organic_results"]
    print(f"Web search results:\n{results}\n\n")
    return results


@function_tool
def web_reader(url: str):
    """
    Read the content of a web page.

    Args:
        url: The URL of the web page to read
    """
    try:
        # Send a GET request to the URL
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()

        # Parse the HTML content
        html = response.text
        parser = HTMLParser(html)

        # Remove unwanted elements
        for tag in parser.css(
            "script, style, noscript, iframe, nav, footer, header, aside, [class*='ad'], [class*='banner'], [class*='menu'], [class*='sidebar'], [class*='nav'], [id*='nav'], [id*='menu'], [id*='sidebar'], [id*='footer'], [id*='header']"
        ):
            tag.decompose()

        # Extract text from the main content
        main_content = ""

        # Try to find the main content element
        main_elements = parser.css("main, article, #content, .content, [role='main']")

        if main_elements:
            # If found specific content containers, use them
            for element in main_elements:
                text = element.text(strip=True)
                if text:
                    main_content += text + "\n\n"
        else:
            # Otherwise get text from the body, filtering out small text blocks
            for tag in parser.css("p, h1, h2, h3, h4, h5, h6, li"):
                text = tag.text(strip=True)
                if (
                    text and len(text) > 20
                ):  # Filter out very short pieces that are likely navigation
                    main_content += text + "\n\n"

        # Clean up the text
        main_content = main_content.strip()

        # Handle empty content
        if not main_content:
            for tag in parser.css("body"):
                main_content = tag.text(strip=True)

        print(f"Web content retrieved:\n{main_content[:500]}\n\n")
        return main_content

    except Exception as e:
        return f"Error retrieving web content: {str(e)}"
