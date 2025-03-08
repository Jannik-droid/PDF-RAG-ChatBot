from helper_function.create_and_update_vector_db import create_vector_store
from helper_function.load_and_split_pdfs import load_and_split_pdfs
from helper_function.query_rag import query_rag


# Example Usage
if __name__ == "__main__":
    pdf_files = ["./data/test.pdf"]  # Add your PDF paths here
    docs = load_and_split_pdfs(pdf_files)
    vector_store = create_vector_store(docs)
    while True:
        try:
            query = input("Question: ")
            response = query_rag(vector_store, query)
            print("Response:", response)
        except EOFError:
            break