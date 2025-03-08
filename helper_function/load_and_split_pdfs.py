import re
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

#Function to clean up text
def clean_text(text):
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
    return text

# Function to load and split PDFs into chunks
def load_and_split_pdfs(pdf_paths, chunk_size=500, chunk_overlap=50):
    documents = []
    for path in pdf_paths:
        loader = PyMuPDFLoader(path)
        raw_docs = loader.load()
        
        # Clean text
        for doc in raw_docs:
            doc.page_content = clean_text(doc.page_content)
            documents.append(doc)
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)