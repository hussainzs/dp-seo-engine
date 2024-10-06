from langchain.text_splitter import CharacterTextSplitter
from typing import List
from langchain_core.documents import Document

def splitter(data_list: List[Document]) -> List[Document]:
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=2000, chunk_overlap=100
    )
    return text_splitter.split_documents(data_list)
