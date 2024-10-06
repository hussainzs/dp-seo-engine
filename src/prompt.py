from langchain_core.prompts import ChatPromptTemplate

def get_prompt() -> ChatPromptTemplate:
    """
    Generates a prompt template for an editor with knowledge in search engine optimization (SEO).

    The template includes placeholders for various contexts such as 
    --> information about articles, SEO tips, and writing style guides.

    Returns:
        ChatPromptTemplate: A prompt template with placeholders for context and question.
    """

    template = """
    Pretend you are an editor for the Daily Pennsylvanian that has deep knowledge in search engine optimization.

    Information about ALL of the Daily Pennsylvanian's articles can be found through this context: {context}

    Information how to search engine optimize (SEO) article titles and URL slugs can be found through: {context1}

    The Daily Pennsylvanian writing style guide and tips can be found through {context2}
    Ensure that all of the titles and URL slugs follow these writing style guides

    Answer the question: {question}.
    """
    return ChatPromptTemplate.from_template(template)
