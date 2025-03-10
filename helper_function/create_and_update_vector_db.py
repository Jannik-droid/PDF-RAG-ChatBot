import hashlib
from langchain_ollama import OllamaEmbeddings
import shutil
import os
from langchain_chroma import Chroma  # Updated import

# Function to create a hash of document content
def hash_document(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

# Function to create or update vector storage
def create_vector_store(documents, persist_directory="./chroma_db"):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    # Load existing ChromaDB
    vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

    # Get existing document hashes
    existing_hashes = set()
    if vector_store._collection.count() > 0:
        existing_metadata = vector_store._collection.get(include=["metadatas"])["metadatas"]
        existing_hashes = {meta["hash"] for meta in existing_metadata if "hash" in meta}

    # Filter new documents
    new_documents = []
    for doc in documents:
        doc_hash = hash_document(doc.page_content)
        if doc_hash not in existing_hashes:
            doc.metadata["hash"] = doc_hash
            new_documents.append(doc)

    # Add only new documents
    if new_documents:
        vector_store.add_documents(new_documents)
    
    return vector_store  # No need to call persist() anymore

# Function to clear the vector storage
def clear_vector_store(persist_directory="./chroma_db"):
    for filename in os.listdir(persist_directory):
        file_path = os.path.join(persist_directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')