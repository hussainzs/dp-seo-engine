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

    vectorstore = Chroma(
        collection_name=collection_name,
        embedding=NomicEmbeddings(model="nomic-embed-text-v1"),
    )
    # Maximum batch size otherwise throws error in site-packages\chromadb\api\types.py", line 571, in validate_batch
    # --> raise ValueError(ValueError: Batch size 1573 exceeds maximum batch size 166)
    batch_size: int = 166  
    for i in range(0, len(documents), batch_size):
        batch_docs: List[Document] = documents[i : i+batch_size] #slice the documents into batches
        vectorstore.add_documents(batch_docs)
    return vectorstore.as_retriever()
