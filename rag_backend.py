# rag_backend.py
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
import os



CHROMA_DIR = "chroma_store"

def load_pdf_to_chunks(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_vectorstore(docs, embedding):
    return Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=CHROMA_DIR)

def load_vectorstore(embedding):
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding)

def get_qa_chain(vectorstore):
    llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="meta-llama/llama-4-scout-17b-16e-instruct")
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

def ingest_and_get_chain(file_path):
    embedding = get_embeddings()
    docs = load_pdf_to_chunks(file_path)
    vectorstore = create_vectorstore(docs, embedding)
    return get_qa_chain(vectorstore)
