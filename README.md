# 📄 Local PDF RAG with Ollama, ChromaDB and StreamLit

A locally running **Retrieval-Augmented Generation (RAG)** system that processes PDFs, stores embeddings in **ChromaDB**, and queries an **Ollama-powered LLM** with a StreamLit UI for intelligent search.  

## 🚀 Features  
- Extracts & cleans text from PDFs 📄  
- Generates **embeddings** using `mxbai-embed-large`  
- Stores & retrieves **vectors** with **ChromaDB**  
- Queries an **Ollama LLM** (`mistral`) 
- Userfriendly **StreamLit UI**

## 🦾 How to use
Since this is a StreamLit App, just type: `stremalit run app.py` and follow the instructions in the app.

## ⚙️ Requirements
Make sure to have Ollama and the corresponding LLMs installed (e.g. `Mistral` and `nomic-embed-text`)