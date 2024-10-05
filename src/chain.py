from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from prompt import get_prompt

def create_chain(csv_retriever, url_retriever, pdf_retriever, api_key, model_name):
    model_remote = ChatAnthropic(api_key=api_key, model_name=model_name)
    chain = (
        {
            "context": csv_retriever,
            "context1": url_retriever,
            "context2": pdf_retriever,
            "question": RunnablePassthrough()
        }
        | get_prompt()
        | model_remote
        | StrOutputParser()
    )
    return chain
