from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def get_retriever():

    embeddings = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory="./vectorstore",
        embedding_function=embeddings
    )

    return vectordb.as_retriever()
