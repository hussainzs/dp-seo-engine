from data_loader import load_csv, load_url, load_pdf
from text_splitter import recursive_splitter, txt_to_documents
from vector_store import create_vector_store
from chain import create_chain
from ui import create_ui
import os, subprocess, sys
from dotenv import load_dotenv
from typing import List
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever

def main():
    # Load environment variables
    print("Loading environment variables...")
    load_dotenv()
    api_key = os.getenv('ANTHROPIC_API_KEY')
    model_name = os.getenv('LLM_MODEL_NAME')

    # Validate environment variables
    if not api_key or not model_name:
        print("VALIDATION ERROR: Please provide an API key and model name in env file")
        sys.exit(1)

    # Login to nomic vector embedding model
    nomic_login_key = os.getenv('NOMIC_LOGIN_KEY')
    if nomic_login_key:
        # executes nomic login key command in the terminal
        subprocess.run(['nomic', 'login', nomic_login_key], check=True)
    else:
        print("VALIDATION ERROR: Nomic login key not found in env file. Please provide a login key to use Nomic vector embeddings")
        sys.exit(1)

    # Load data
    print("Loading data from csv, pdf, urls...")
    csv_data: List[Document] = load_csv("files/organic_search.csv")
    pdf_list: List[str] = [
        'files/34_Style.pdf',
        'files/All_Style.pdf',
        'files/DEI_Style.pdf',
        'files/Sports_Style.pdf'
    ]
    pdfs_list: List[Document] = load_pdf(pdf_list)
    urls: List[str] = [
    'https://yoast.com/slug/',
    'https://www.semrush.com/blog/what-is-a-url-slug/?kw=&cmp=US_SRCH_DSA_Blog_EN&label=dsa_pagefeed&Network=g&Device=c&kwid=dsa-2185834088336&cmpid=18348486859&agpid=156019556762&BU=Core&extid=97592280163&adpos=',
    'https://www.upwork.com/resources/how-to-write-seo-content','https://authorservices.wiley.com/author-resources/Journal-Authors/Prepare/writing-for-seo.html',
    'https://www.semrush.com/blog/seo-writing/','https://www.semrush.com/kb/839-how-to-write-seo-articles-four-steps',
    'https://www.flowmatters.com/blog/a-practical-guide-on-how-to-write-seo-articles/',
    'https://www.maropost.com/how-to-combine-seo-and-email-marketing-for-better-rankings/',
    'https://www.webfx.com/seo/learn/email-marketing-tips-to-improve-seo/',
    'https://sendgrid.com/en-us/blog/seo-and-email-marketing','https://www.emailonacid.com/blog/article/email-marketing/seo-connections/',
    'https://coalitiontechnologies.com/blog/strategic-seo-tips-for-email-marketing',
    'https://optinmonster.com/101-email-subject-lines-your-subscribers-cant-resist/',
    'https://www.wordstream.com/blog/ws/2014/03/31/email-subject-lines',
    'https://www.constantcontact.com/blog/good-email-subject-lines/',
    'https://blog.hubspot.com/marketing/best-email-subject-lines-list',
    'https://www.google.com/search/howsearchworks/how-search-works/ranking-results/#:~:text=To%20give%20you%20the%20most,the%20nature%20of%20your%20query.',
    'https://www.semrush.com/blog/google-search-algorithm/',
    'https://www.seomechanic.com/google-search-algorithm-work/',
    'https://developers.google.com/search/docs/fundamentals/how-search-works',
    'https://ahrefs.com/blog/google-search-algorithm/',
    'https://www.shopify.com/blog/google-algorithm',
    'https://www.webfx.com/seo/glossary/what-is-a-google-algorithm/',
    'https://www.purplepublish.com/en/blog/seo-for-publishers',
    'https://www.webceo.com/blog/how-to-do-seo-for-news-websites/',
    'https://www.stanventures.com/blog/seo-for-journalist/',
    'https://blog.replug.io/what-is-a-url-slug-and-how-to-optimize-it/'
]
    docs_list: List[Document] = load_url(urls)

    # Split data
    print("Splitting data using recursive splitter...")
    doc_splits: List[Document] = recursive_splitter(csv_data)
    url_splits: List[Document] = recursive_splitter(docs_list)
    pdf_splits: List[Document] = recursive_splitter(pdfs_list)
    tag_splits: List[Document] = txt_to_documents('files/final_tags.txt')
    print(f"Doc_split length: {len(doc_splits)}\nurl_split length: {len(url_splits)}\npdf_splits length: {len(pdf_splits)}\n tag_split length: {len(tag_splits)}")

    # Create vector stores
    print("Storing data in vector stores...")
    csv_retriever: VectorStoreRetriever = create_vector_store(doc_splits, "csv_collection")
    url_retriever: VectorStoreRetriever = create_vector_store(url_splits, "url_collection")
    pdf_retriever: VectorStoreRetriever = create_vector_store(pdf_splits, "pdf_collection")
    tag_retriever: VectorStoreRetriever = create_vector_store(tag_splits, "tag_collection", 10)
    print("Data stored in vector stores ✅")

    # Create chain
    chain = create_chain(csv_retriever, url_retriever, pdf_retriever, tag_retriever, api_key, model_name)
    
    # Define chat function
    def chat(input_text, dept, title, content, chat_history):
        chat_history = chat_history or []
        prompt_text = f""" I am a student journalist who writes for this department: {dept} so use the writing guide that is meant for: {dept}.
        The title of the article that I'm thinking of is: {title}, the content of the article is: {content}. My question is: {input_text}"""
        response = chain.invoke(prompt_text)
        chat_history.append((input_text, response))
        return chat_history, chat_history, "", "", "", ""

    # Create and launch the UI
    print("Launching UI...")
    demo = create_ui(chat)
    demo.launch(debug=True, share=True)

if __name__ == "__main__":
    main()
