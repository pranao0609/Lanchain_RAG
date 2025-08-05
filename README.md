# RAG Chatbot 

A simple yet powerful **Retrieval-Augmented Generation (RAG) Chatbot** built with **LangChain**, **HuggingFace embeddings**,**GROQ API** and **Streamlit**. This app lets you upload a PDF, creates a vectorstore from the content, and allows you to ask natural language questions about the document.



##  What is RAG?

**Retrieval-Augmented Generation (RAG)** is an architecture that combines information retrieval with generative models like GPT. Instead of relying solely on pre-trained knowledge, RAG retrieves relevant context from a custom document (like your uploaded PDF) and feeds it to the language model to generate accurate answers.



## Features

- Upload any PDF file.
- Convert PDF into chunks and embed them using OpenAI embeddings.
- Store embeddings in a vectorstore (FAISS).
- Query the vectorstore using a question-answering chain powered by LangChain.
- Interactive web UI using Streamlit.

## How It Works

1. Upload a PDF via the UI.
2. The backend extracts text, splits it into chunks, and generates embeddings using OpenAI.
3. The chunks and their embeddings are stored in a FAISS vectorstore.
4. When a user asks a question, LangChain retrieves the most relevant chunks and sends them (along with the query) to a language model for final answer generation.

---
