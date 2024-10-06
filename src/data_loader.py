import os
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from typing import List
from langchain_core.documents import Document

# Throws warning: USER_AGENT environment variable not set, consider setting it to identify your requests.
# Don't know how to fix it, I Tried the obvious solution but that didn't fix the warning.

def load_csv(csv_path: str) -> List[Document]:
    """
    Load CSV files into a list of Documents. Every row is converted into a key/value pair and outputted to a new line in the documents page_content.

    Args:
        csv_path (str): The path to the CSV file.

    Returns:
        List[Document]: Each row of the CSV file is translated to one document.
    """
    loader = CSVLoader(file_path=csv_path, encoding='utf-8')
    data: List[Document] = loader.load()
    return data

def load_url(url_list: List[str]) -> List[Document]:
    """
    Load all text from HTML webpages into a document format 

    Args:
        url_list (List[str]): A list of URLs to retrieve data from.

    Returns:
        List[Document]: A list of documents retrieved from the URLs.
    """
    docs = [WebBaseLoader(web_path=url, show_progress=True).load() for url in url_list]
    docs_list = [item for sublist in docs for item in sublist]
    return docs_list

def load_pdf(pdf_list: List[str]) -> List[Document]:
    """
    Loads data from a list of PDF files into Document objects.

    Args:
        pdf_list (list[str]): A list of paths to PDF files.

    Returns:
        List[Document]: A list of documents retrieved from the PDF files.
    """
    output = [PyPDFLoader(file_path=pdf).load() for pdf in pdf_list]
    pdfs_list = [item for sublist in output for item in sublist]
    return pdfs_list
