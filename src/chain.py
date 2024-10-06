from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from prompt import get_prompt

def create_chain(csv_retriever, url_retriever, pdf_retriever, api_key, model_name):
    """
    Creates a langchain chain that retrieves data from 3 sources and passes them as context for RAG along with prompt.

    Args:
        csv_retriever (object): retrieve data from CSV files.
        url_retriever (object): retrieve data from URLs.
        pdf_retriever (object): retrieve data from PDF files.
        api_key (str): The API key for the ChatAnthropic model.
        model_name (str): The name of LLM model

    Returns:
        chain (object): Langchain chain that combines the data retrieval and processing steps. 
    """
    model_remote = ChatAnthropic(api_key=api_key, model_name=model_name)
    chain = (
        {
            "context": csv_retriever,
            "context1": url_retriever,
            "context2": pdf_retriever,
            "question": RunnablePassthrough()
        }
        | get_prompt()
        | model_remote
        | StrOutputParser()
    )
    return chain
