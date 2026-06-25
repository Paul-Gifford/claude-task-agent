import os
import requests

# JSON schema Claude uses to call this tool
SCHEMA = {
    "name": "web_search",
    "description": "Search the web for current information. Use this before writing any research-based content.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query. Be specific for better results.",
            }
        },
        "required": ["query"],
    },
}


def web_search(query: str) -> str:
    """
    Search the web using the Brave Search API.
    Returns a formatted string of the top results.
    """
    api_key = os.getenv("BRAVE_API_KEY")
    if not api_key:
        return "ERROR: BRAVE_API_KEY not set in .env"

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key,
    }

    params = {
        "q": query,
        "count": 5,
        "text_decorations": False,
        "search_lang": "en",
    }

    try:
        response = requests.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers=headers,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        results = data.get("web", {}).get("results", [])
        if not results:
            return f"No results found for: {query}"

        # Format results for Claude to read
        formatted = [f"Search results for: '{query}'\n"]
        for i, result in enumerate(results, 1):
            title = result.get("title", "No title")
            url = result.get("url", "")
            description = result.get("description", "No description")
            formatted.append(f"{i}. {title}\n   URL: {url}\n   {description}\n")

        return "\n".join(formatted)

    except requests.exceptions.Timeout:
        return f"ERROR: Search timed out for query: {query}"
    except requests.exceptions.RequestException as e:
        return f"ERROR: Search failed: {str(e)}"