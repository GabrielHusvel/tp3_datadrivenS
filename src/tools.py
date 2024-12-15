from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_community.utilities.arxiv import ArxivAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper
from typing import Optional
from langchain_core.language_models import BaseLanguageModel

def load_tools(tool_names: list[str], llm: Optional[BaseLanguageModel] = None):
    """
    Carrega as ferramentas disponíveis para o agente.
    """
    available_tools = {
        "arxiv": ArxivQueryRun(api_wrapper=ArxivAPIWrapper()),
        "wikipedia": WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()),
        "ddg_search": DuckDuckGoSearchRun(api_wrapper=DuckDuckGoSearchAPIWrapper())
    }
    return [available_tools[name] for name in tool_names if name in available_tools]

