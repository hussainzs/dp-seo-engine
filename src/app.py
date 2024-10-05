# src/app.py

from data_loader import load_csv, load_url, load_pdf
from text_splitter import splitter
from vector_store import create_vector_store
from chain import create_chain
from ui import create_ui
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('ANTHROPIC_API_KEY')
    model_name = "claude-3-5-sonnet-20240620"

    # Load data
    csv_data = load_csv("data/organic_search.csv")
    pdf_list = [
        'data/files/34_Style.pdf',
        'data/files/All_Style.pdf',
        'data/files/DEI_Style.pdf',
        'data/files/Sports_Style.pdf'
    ]
    pdfs_list = load_pdf(pdf_list)
    urls = [
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
    docs_list = load_url(urls)

    # Split data
    doc_splits = splitter(csv_data)
    url_splits = splitter(docs_list)
    pdf_splits = splitter(pdfs_list)

    # Create vector stores
    csv_retriever = create_vector_store(doc_splits, "csv_collection")
    url_retriever = create_vector_store(url_splits, "url_collection")
    pdf_retriever = create_vector_store(pdf_splits, "pdf_collection")

    # Create chain
    chain = create_chain(csv_retriever, url_retriever, pdf_retriever, api_key, model_name)

    # Define chat function
    def chat(input_text, dept, title, content, chat_history):
        chat_history = chat_history or []
        prompt_text = f""" I am a student who writes for this department: {dept} so use the writing guide that is meant for: {dept}
        The title is: {title}, the content is: {content}. Answer the question based on the contexts {input_text}"""
        response = chain.invoke(prompt_text)
        chat_history.append((input_text, response))
        return chat_history, chat_history, "", "", "", ""

    # Create and launch the UI
    demo = create_ui(chat)
    demo.launch(debug=True, share=True)

if __name__ == "__main__":
    main()
