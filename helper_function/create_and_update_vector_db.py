from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

#Function to create vector storage
def create_vector_store(documents, persist_directory="./chroma_db"):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vector_store = Chroma.from_documents(documents, embeddings, persist_directory=persist_directory)
    return vector_store