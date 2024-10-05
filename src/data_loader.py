from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader

def load_csv(csv_path):
    loader = CSVLoader(file_path=csv_path)
    data = loader.load()
    return data

def load_url(url_list):
    docs = [WebBaseLoader(url).load() for url in url_list]
    docs_list = [item for sublist in docs for item in sublist]
    return docs_list

def load_pdf(pdf_list):
    output = [PyPDFLoader(pdf).load() for pdf in pdf_list]
    pdfs_list = [item for sublist in output for item in sublist]
    return pdfs_list
