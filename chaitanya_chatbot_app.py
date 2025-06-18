import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import Docx2txtLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

# --- Page Config ---
st.set_page_config(page_title="ChaitanyaGPT", page_icon="🕉️", layout="wide")
st.markdown("""
    <style>
        .block-container {
            padding: 2rem 2rem 2rem 2rem;
        }
        .stChatMessage { background: #f8f9fa; border-radius: 15px; padding: 1rem; margin-bottom: 1rem; }
        .stChatMessage.user { background-color: #e3f2fd; }
        .stChatMessage.assistant { background-color: #fff3e0; }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🕉️ ChaitanyaGPT")
st.caption("Your AI companion based on the *Teachings of Lord Chaitanya (1968)*")

# --- Load & Prepare Bot ---
@st.cache_resource(show_spinner=True)
def prepare_bot(docx_path):
    loader = Docx2txtLoader(docx_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
    return db, chain

# --- Setup Bot ---
db, chain = prepare_bot("Teachings-of-Lord-Chaitanya-original-1968.docx")

# --- Chat History ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Chat Input ---
st.markdown("#### Ask me anything from the sacred teachings ✨")
user_input = st.chat_input("Enter your question")

if user_input:
    st.chat_message("user").markdown(user_input)
    with st.spinner("Seeking divine knowledge ✨"):
        docs = db.similarity_search(user_input)
        answer = chain.run(input_documents=docs, question=user_input)
    st.chat_message("assistant").markdown(answer)
    st.session_state.history.append((user_input, answer))

# --- Show Chat History ---
for q, a in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(a)
