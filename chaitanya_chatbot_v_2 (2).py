# Teachings of Lord Chaitanya Chatbot – V2 (Hinglish, No OpenAI, Multi-Paragraph)

import streamlit as st
from PyPDF2 import PdfReader
import numpy as np
import faiss
import re
from sentence_transformers import SentenceTransformer

# ---------------------- PDF Processing ----------------------

def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text
    except Exception as e:
        st.error(f"Failed to read PDF: {e}")
        return ""

def split_text(text, max_chunk_size=1000):
    sentences = re.split(r'[\n\.!?]', text)
    chunks, chunk = [], ""
    for sentence in sentences:
        if len(chunk) + len(sentence) <= max_chunk_size:
            chunk += sentence.strip() + " "
        else:
            chunks.append(chunk.strip())
            chunk = sentence.strip() + " "
    if chunk:
        chunks.append(chunk.strip())
    return chunks

# ---------------------- Embedding & Search ----------------------

@st.cache_resource(show_spinner=False)
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def build_index(chunks, model):
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, embeddings, chunks

def search_answers(query, model, index, chunks, top_k=3):
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, top_k)
    return [chunks[i] for i in I[0]]

# ---------------------- Streamlit UI ----------------------

st.set_page_config(page_title="Lord Chaitanya Q&A Chatbot")
st.title("📖 Teachings of Lord Chaitanya – Hinglish Q&A Chatbot")
st.markdown("Ask any question in Hinglish and get answers from the book itself.")

uploaded_file = st.file_uploader("📥 Upload 'Teachings of Lord Chaitanya' PDF:", type="pdf")

if uploaded_file is not None:
    with st.spinner("Processing PDF, please wait..."):
        text = extract_text_from_pdf(uploaded_file)
        if not text.strip():
            st.error("No readable text found in the PDF. Please upload a clear, text-based file.")
        else:
            chunks = split_text(text)
            model = load_model()
            index, embeddings, chunk_list = build_index(chunks, model)
            st.success("Chatbot ready! Type your question below.")

            user_query = st.text_input("💬 Ask your question (Hinglish supported):")

            if user_query:
                top_answers = search_answers(user_query, model, index, chunk_list, top_k=3)
                st.markdown("### 📜 Answer from Teachings:")
                for i, ans in enumerate(top_answers, 1):
                    st.markdown(f"**{i}.** {ans}")
else:
    st.info("Please upload the PDF file to begin.")
