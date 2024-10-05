from langchain.text_splitter import CharacterTextSplitter

def splitter(data_list):
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=2000, chunk_overlap=100
    )
    splits = text_splitter.split_documents(data_list)
    return splits
