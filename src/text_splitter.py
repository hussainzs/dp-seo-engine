from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document


def splitter(data_list: List[Document]) -> List[Document]:
    """
    # Using this throws error: "Created a chunk of size 3065, which is longer than the specified 2000"
    # Avoid using this. Use recursive_splitter instead.
    
    Splits a list of documents into smaller chunks using a character-based text splitter.
    Each chunk has a size of 2000 characters with an overlap of 100 characters.
    Documentation: https://python.langchain.com/docs/how_to/character_text_splitter/

    Args:
        data_list (List[Document]): A list of documents to be split.

    Returns:
        List[Document]: A list of documents split into smaller chunks.
    """

    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=2000, chunk_overlap=100
    )
    return text_splitter.split_documents(data_list)

def recursive_splitter(data_list: List[Document]) -> List[Document]:
    """
    Splits a list of documents into smaller chunks using a recursive character-based text splitter.
    Documentation: https://python.langchain.com/docs/how_to/recursive_text_splitter/

    Args:
        data_list (List[Document]): A list of documents to be split.

    Returns:
        List[Document]: A list of documents split into smaller chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000, chunk_overlap=100
    )
    return text_splitter.split_documents(data_list)
