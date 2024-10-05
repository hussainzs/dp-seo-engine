from langchain_community.vectorstores import Chroma
from langchain_nomic import NomicEmbeddings

def create_vector_store(documents, collection_name):
    vectorstore = Chroma.from_documents(
        documents=documents,
        collection_name=collection_name,
        embedding=NomicEmbeddings(model="nomic-embed-text-v1"),
    )
    return vectorstore.as_retriever()
