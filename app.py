import streamlit as st
import chromadb
from helper_function.create_and_update_vector_db import create_vector_store, clear_vector_store
from helper_function.load_and_split_pdfs import load_and_split_pdfs
from helper_function.query_rag import query_rag

def main():
    clear_vector_store()
    chromadb.api.client.SharedSystemClient.clear_system_cache()

    st.title("📄 Local PDF RAG")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a file", type=["pdf"])
    
    if uploaded_file is not None:
        st.success(f"Uploaded: {uploaded_file.name}")

        # Save the uploaded file to the /data folder
        file_path = f"/Users/jannikb/Desktop/PDF-RAG-ChatBot/data/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File saved to: {file_path}")

        pdf_files = [file_path]  # Add your PDF paths here
        docs = load_and_split_pdfs(pdf_files)
        vector_store = create_vector_store(docs)        
        
        # User input for question
        question = st.text_input("Ask a question about the file:")
        
        if st.button("Get Answer"):
            if question:
                response = query_rag(vector_store, question)
                st.write(response)
                chromadb.api.client.SharedSystemClient.clear_system_cache()

            else:
                st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
