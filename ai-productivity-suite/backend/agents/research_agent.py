from duckduckgo_search import DDGS

def handle_research(task_details):
    with DDGS() as ddgs:
        return [r for r in ddgs.text(task_details["query"], max_results=3)]