import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
import requests

app = Flask(__name__)
CORS(app)

# Configuration
DOCS_DIR = os.path.join(os.path.dirname(__file__), 'documents')
DB_DIR = os.path.join(os.path.dirname(__file__), 'chroma_db')
OLLAMA_URL = "http://localhost:11434/api/generate"

# Verify That the following Folders is Exists
os.makedirs(DOCS_DIR, exist_ok=True)

# 1. Loading documents and creating the database (ChromaDB)
@app.route('/ingest', list=["GET", "POST"])
def ingest_docs():
    try:
        loader = DirectoryLoader(DOCS_DIR, glob="*.pdf", loader_cls=PyPDFLoader)
        docs = loader.load()
        
        if not docs:
            return jsonify({"status": "error", "message": "No PDF files found in the documents folder!"})
        
        # Breaking text into small fragments
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        splits = text_splitter.split_documents(docs)
        
        # Local embedding and saving to the database
        embeddings = OllamaEmbeddings(model="llama3:8b")
        vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory=DB_DIR)
        vectorstore.persist()
        
        return jsonify({"status": "success", "message": f"{len(splits)} Data chunks successfully saved in ChromaDB!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# 2. Asking the question to an  AI ​​agent
@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.json
    user_query = data.get("question")
    
    if not user_query:
        return jsonify({"error": "Please ask a question."})
    
    try:
        # Searching for context in the database
        embeddings = OllamaEmbeddings(model="llama3:8b")
        vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
        docs = vectorstore.similarity_search(user_query, k=3)
        
        context = "\n".join([doc.page_content for doc in docs])
        
        # Creating prompts for AI
        prompt = f"""You are a clinical trial research assistant. Provide an accurate answer to the user's question using the context provided below. Do not fabricate an answer if you do not know it.

reference:
{context}

question: {user_query}
answer:"""
        
        # Calling the Ollama API
        response = requests.post(OLLAMA_URL, json={
            "model": "llama3:8b",
            "prompt": prompt,
            "stream": False
        })
        
        ai_response = response.json().get("response", "Could not get the answer.")
        return jsonify({"answer": ai_response})
        
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
