from langchain_community.vectorstores import Chroma
from langchain_nomic import NomicEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.documents import Document
from typing import List

def create_vector_store(documents: List[Document], collection_name: str) -> VectorStoreRetriever:
    vectorstore = Chroma.from_documents(
        documents=documents,
        collection_name=collection_name,
        embedding=NomicEmbeddings(model="nomic-embed-text-v1"),
    )
    return vectorstore.as_retriever()
