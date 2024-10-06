from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from typing import List
from langchain_core.documents import Document

def load_csv(csv_path) -> List[Document]:
    """
    Loads data from a CSV file.

    Args:
        csv_path (str): The path to the CSV file.

    Returns:
        data (list): A list of data rows loaded from the CSV file.
    """
    loader = CSVLoader(file_path=csv_path)
    data: List[Document] = loader.load()
    return data

def load_url(url_list) -> List[Document]:
    """
    Loads data from a list of URLs.

    Args:
        url_list (list): A list of URLs to retrieve data from.

    Returns:
        docs_list (list): A list of documents retrieved from the URLs.
    """
    docs = [WebBaseLoader(url).load() for url in url_list]
    docs_list = [item for sublist in docs for item in sublist]
    return docs_list

def load_pdf(pdf_list) -> List[Document]:
    """
    Loads data from a list of PDF files.

    Args:
        pdf_list (list): A list of paths to PDF files.

    Returns:
        pdfs_list (list): A list of documents retrieved from the PDF files.
    """
    output = [PyPDFLoader(pdf).load() for pdf in pdf_list]
    pdfs_list = [item for sublist in output for item in sublist]
    return pdfs_list
