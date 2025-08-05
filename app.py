# app.py

import streamlit as st
from rag_backend import ingest_and_get_chain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App config
st.set_page_config(page_title="📚 RAG Chatbot", page_icon="🤖", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton > button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stTextInput>div>div>input {
            border: 2px solid #1f77b4;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">"RAG Chatbot"</div>', unsafe_allow_html=True)

# PDF Upload
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    os.makedirs("./data", exist_ok=True)
    file_path = f"./data/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    qa_chain = ingest_and_get_chain(file_path)
    st.session_state.qa_chain = qa_chain


# Chat UI
if "qa_chain" in st.session_state:
    with st.form(key="chat_form"):
        user_query = st.text_input(" Ask something from the document:")
        submit = st.form_submit_button("Get Answer")
        
        if submit and user_query:
            response = st.session_state.qa_chain.run(user_query)
            st.markdown(f"""
                <div style='background-color: #e8f0fe; padding: 15px; border-radius: 10px;'>
                    <b>Answer:</b> {response}
                </div>
            """, unsafe_allow_html=True)
