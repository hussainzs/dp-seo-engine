from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever
from prompt import get_prompt

def create_chain(csv_retriever: VectorStoreRetriever, 
                 url_retriever: VectorStoreRetriever, 
                 pdf_retriever: VectorStoreRetriever, 
                 api_key: str, model_name: str):
    """
    Creates a langchain chain that retrieves data from 3 sources and passes them as context for RAG along with prompt.

    Args:
        csv_retriever (VectorStoreRetriever): retrieve relevant data from CSV files.
        url_retriever (VectorStoreRetriever): retrieve relevant data from URLs.
        pdf_retriever (VectorStoreRetriever): retrieve relevant data from PDF files.
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
