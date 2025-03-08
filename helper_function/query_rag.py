from langchain_ollama import OllamaLLM

#Function to query the LLM with Retrieved Context
def query_rag(vector_store, query, top_k=3, model="mistral"):
    retriever = vector_store.as_retriever(search_kwargs={"k": top_k})
    relevant_docs = retriever.invoke(query)
    
    context = "\n".join([doc.page_content for doc in relevant_docs])
    llm = OllamaLLM(model=model)
    
    prompt = f"""
    You are an AI assistant answering questions based on the given context.
    Context:
    {context}
    
    Question: {query}
    
    Answer:
    """
    #print(prompt)
    return llm.invoke(prompt)