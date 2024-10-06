from langchain_community.vectorstores import Chroma
from langchain_nomic import NomicEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.documents import Document
from typing import List

def create_vector_store(documents: List[Document], collection_name: str) -> VectorStoreRetriever:
    """
    Creates a vector store from a list of documents and returns a retriever for querying the store.
    Documentation for Chroma: https://python.langchain.com/docs/integrations/vectorstores/chroma/

    Args:
        documents (List[Document]): A list of documents to be stored in the vector store.
        collection_name (str): The name of the collection to be created in the vector store.

    Returns:
        VectorStoreRetriever: A retriever object for querying the vector store.
    """

    vectorstore = Chroma.from_documents(
        documents=documents,
        collection_name=collection_name,
        embedding=NomicEmbeddings(model="nomic-embed-text-v1"),
    )
    return vectorstore.as_retriever()
