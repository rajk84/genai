import streamlit as st
import PyPDF2

st.title("📄 Chat with Your PDF")

# Upload a PDF
pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf is not None:
    reader = PyPDF2.PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.subheader("📃 Extracted Text Preview")
    st.write(text[:1000])  # Show a preview

from typing import List

# Function to split text into overlapping chunks
def split_text(text: str, chunk_size=500, overlap=50) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

chunks = split_text(text)
st.write(f"🔹 Split into {len(chunks)} chunks.")
