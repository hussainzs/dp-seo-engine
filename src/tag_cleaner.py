from typing import List
import re, os
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

"""
Please run this file with caution!, as using the LLM model on a large number of tags incurs costs.
To prevent unintentional execution, a function that combines all these methods has not been provided.
If you wish to re-run these methods on a new set of tags, you will need to carefully understand and execute each method.
"""

def read_file(file_path: str) -> str:
    """
    Reads the entire content of a text file and returns it as a string. 
    Use this when you want a string representation of entire file content.
    
    Args:
    file_path (str): The path to the text file.
    
    Returns:
    str: The content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def extract_tags_from_text(text: str) -> List[str]:
    """
    Extracts individual tags from a comma-separated string.
    Removes surrounding square brackets, quotation marks, leading/trailing spaces, empty tags, 
    tags containing digit/digit, digit-digit, or digit.digit patterns, and tags of length 1

    Args:
        text (str): A string containing tags separated by commas.
        Expected input format: ['', 'art contrapposto', '11.6.2013', 'app of the week', ...]

    Returns:
        List[str]: A list of cleaned tags.
    """
    filtered_tags: List[str] = []
    
    # Regular expression to detect strings that contain digit/digit, digit-digit, or digit.digit patterns
    pattern = re.compile(r'\d+[/-]\d+|\d+\.\d+')
    
    # Remove the square brackets at the start and end of the string, if present
    text: str = text.strip('[]')
    
    # Split the string by commas to get individual tags
    raw_tags: List[str] = text.split(',')
    
    # Clean each tag by removing surrounding quotation marks and stripping leading/trailing spaces
    for tag in raw_tags:
        cleaned_tag = tag.strip().strip("'\"")
        
        # Skip empty tags or tags that are just quotation marks or one letter
        if not cleaned_tag or cleaned_tag in ["''", '""', "' '"] or len(cleaned_tag) == 1:
            continue
        
        # Skip tags containing digit/digit, digit-digit, or digit.digit patterns
        if pattern.search(cleaned_tag):
            continue
        
        # Otherwise, add the cleaned tag to the list
        filtered_tags.append(cleaned_tag)
    
    return filtered_tags

def append_to_file(file_path: str, content: List[str]) -> None:
    """
    Appends a list of strings to the end of text file. Each string is written on a new line.

    Args:
        file_path (str): The path to the text file.
        content (List[str]): The list of strings to write to the file.

    Returns:
        None
    """
    # create the file if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'a', encoding='utf-8') as file:
        for word in content:
            file.write(word.strip() + '\n')

def clean_tags_through_llm(text: List[str]) -> List[str]:
    """
    Asks LLM to check each tag to see if it's relevant. Removes any irrelevant tags and returns a list of valid tags in lower case.
    Also writes the tags to a file 'files/filtered_tags.txt' after each batch of tags is processed.

    Args:
        text (List[str]): list of tags to be checked by the LLM.

    Returns:
        List[str]: list of valid tags.
    """
    
    valid_tags: List[str] = []
    batch_size: int = 20

    # Load environment variables
    api_key = os.getenv('ANTHROPIC_API_KEY')
    model_name = os.getenv('LLM_MODEL_NAME')
    if not api_key or not model_name:
        raise EnvironmentError("Required environment variables 'ANTHROPIC_API_KEY' or 'LLM_MODEL_NAME' are not set.")
    llm = ChatAnthropic(api_key=api_key, model_name=model_name, temperature=0.5)

    template = """
    You are given a batch of tags, which are SEO keywords for articles written by Daily Pennsylvania, a university newspaper covering news, sports, opinion, satire, and arts/culture. 
    You will return a comma separated list of tags that are relevant to the article. 
    i.e. output should look like this (Strictly follow this format.): tag1, tag2, tag3, tag4, tag5
    Do not say anything else at all other than the tags in the desired format. Do not make up your own tags.

    For each tag:
    1. Don't include tags that are abnormal, irrelevant, or not related to the theme of general journalism or SEO.
    2. Return all relevant tags in lowercase. 
    3. If there is a typo or a tag is weird because of unicode, fix the typo if you can reasonably and return the tag in lowercase. Otherwise, ignore it.
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                template,
            ),
            ("human", "{input}"),
        ]
    )
    chain = prompt | llm | StrOutputParser()

    # run each tag through the LLM and keep only the valid ones
    for i in range(0, len(text), batch_size):
        batch: List[str] = text[i: i + batch_size] # get a splice of tags (based on batch size)
        response: str = chain.invoke(batch) # get the response from the LLM for this batch as input
        resultant_tags: List[str] = response.split(',') # the output from LLM should be comma separated tags so split it
        valid_tags.extend(resultant_tags) 
        append_to_file('files/filtered_tags.txt', resultant_tags)
    
    return valid_tags

def process_tags() -> None:
    """
    Reads each line from 'files/filtered_tags.txt', removes duplicates, and writes the unique tags to 'files/final_tags.txt'.

    This function performs the following steps:
    1. Reads each line from 'files/filtered_tags.txt' and adds it to a list.
    2. Converts the list to a set to remove duplicates.
    3. Writes the unique tags to 'files/final_tags.txt', each on a new line.
    """
    input_file_path: str = 'files/filtered_tags.txt'
    output_file_path: str = 'files/final_tags.txt'

    # Step 1: Read the file and add each line to a list
    with open(input_file_path, 'r', encoding='utf-8') as file:
        tags: List[str] = file.readlines()

    # Step 2: Remove duplicates by converting the list to a set
    unique_tags = set(tag.strip() for tag in tags)

    # Step 3: Write the unique tags to the new file
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for tag in unique_tags:
            file.write(tag + '\n')

