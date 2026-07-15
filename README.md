
# 📄 PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that enables users to ask natural language questions about PDF documents and receive accurate, context-aware answers. The application extracts text from uploaded PDFs, splits the content into manageable chunks, generates vector embeddings, stores them in a FAISS vector database, retrieves the most relevant passages for each query, and uses a Hugging Face language model to generate responses based on the retrieved context.

## ✨ Features

* Upload and process PDF documents
* Intelligent text chunking for efficient retrieval
* Semantic search using vector embeddings
* chroma vector database for fast similarity search
* Context-aware question answering with Retrieval-Augmented Generation (RAG)
* Hugging Face embeddings and chat model integration
* FastAPI backend for scalable API development
* Streamlit frontend with an interactive chat interface
* Session-based chat history


## 🚀 How It Works

1. Upload one or more PDF documents.
2. Extract text from the PDFs.
3. Split the text into smaller chunks.
4. Generate embeddings for each chunk.
5. Store the embeddings in a FAISS vector database.
6. Retrieve the most relevant chunks based on the user's question.
7. Send the retrieved context to the language model.
8. Return an accurate, context-aware answer to the user.

## 📌 Use Cases

* Document Question Answering
* Research Assistance
* Company Knowledge Base
* Technical Documentation Search
* Educational Materials
* Policy and Compliance Documents
* User Manuals and Guides

