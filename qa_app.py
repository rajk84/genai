import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_qa_pipeline():
    return pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Load model
qa_pipeline = load_qa_pipeline()

# UI
st.title("❓ Ask Me Anything – Q&A with Transformers")

st.subheader("Context")
context = st.text_area("Paste a paragraph for the model to read:", 
    "Agentic AI systems are designed to take autonomous actions based on goals. They differ from reactive systems by proactively planning, adapting, and reasoning.")

st.subheader("Your Question")
question = st.text_input("Ask a question about the paragraph above:", "How is agentic AI different?")

if st.button("Get Answer"):
    if context.strip() and question.strip():
        result = qa_pipeline(question=question, context=context)
        st.success(f"Answer: {result['answer']}")
    else:
        st.warning("Please enter both context and a question.")
