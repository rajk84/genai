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
