from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.chat_history import BaseChatMessageHistory
from in_memory_history import InMemoryHistory
from prompt import get_prompt
from typing import Dict

def create_chain(csv_retriever: VectorStoreRetriever, 
                 url_retriever: VectorStoreRetriever, 
                 pdf_retriever: VectorStoreRetriever, 
                 tag_retriever: VectorStoreRetriever,
                 api_key: str, model_name: str,
                 message_history: Dict[str, BaseChatMessageHistory]):
    """
    Creates a langchain chain that retrieves data from 3 sources and passes them as context for RAG along with prompt.

    Args:
        csv_retriever (VectorStoreRetriever): retrieve relevant data from CSV files.
        url_retriever (VectorStoreRetriever): retrieve relevant data from URLs.
        pdf_retriever (VectorStoreRetriever): retrieve relevant data from PDF files.
        api_key (str): The API key for the ChatAnthropic model.
        model_name (str): The name of LLM model

    Returns:
        chain (object): Langchain chain that combines the data retrieval and processing steps, as well as providing memory. 
    """
    def combine_docs_and_question(input_dict):
        # Get the question and history from the input
        question = input_dict["question"]
        chat_history = input_dict.get("history", [])
        print(input_dict['history'])
        
        # Get relevant documents from each retriever
        csv_docs = csv_retriever.get_relevant_documents(question)
        url_docs = url_retriever.get_relevant_documents(question)
        pdf_docs = pdf_retriever.get_relevant_documents(question)
        tag_docs = tag_retriever.get_relevant_documents(question)
        
        # Print tags for debugging
        print("**************************************************************************************")
        print("\nRetrieved tags:")
        for doc in tag_docs:
            print(f"- {doc.page_content}")
        print("\n**************************************************************************************")
        
        # Clean up history to only show content
        cleaned_history = []
        for message in chat_history:
            if hasattr(message, 'content'):
                # Determine if it's a human or AI message
                speaker = "Human" if message.type == "human" else "Assistant"
                cleaned_history.append(f"{speaker}: {message.content}")
        
        # Add debug prints for template inputs
        result = {
            "context": "\n".join(doc.page_content for doc in csv_docs),
            "context1": "\n".join(doc.page_content for doc in url_docs),
            "context2": "\n".join(doc.page_content for doc in pdf_docs),
            "context3": "\n".join(doc.page_content for doc in tag_docs),
            "question": question,
            "history": cleaned_history
        }
        
        # print("\n=== TEMPLATE INPUTS ===")
        # print(f"Question: {result['question']}")
        # print("Chat History:")
        # for msg in cleaned_history:
        #     print(f"- {msg}")
        # print("Context Lengths:")
        # print(f"CSV context: {len(result['context'])} chars")
        # print(f"URL context: {len(result['context1'])} chars")
        # print(f"PDF context: {len(result['context2'])} chars")
        # print(f"Tags context: {len(result['context3'])} chars")
        # print("========================\n")
        
        return result
    
    model = ChatAnthropic(api_key=api_key, model_name=model_name)
    
    # Create the base chain
    chain = (
        RunnablePassthrough.assign(
            question=lambda x: x["question"],
            history=lambda x: x.get("history", [])
        )
        | combine_docs_and_question 
        | get_prompt() 
        | model
    )
    
    # Wrap with message history
    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: message_history.get(session_id, InMemoryHistory()),
        input_messages_key="question",
        history_messages_key="history"
    )
    
    return chain_with_history
