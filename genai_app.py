import streamlit as st
from transformers import pipeline, set_seed

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

st.title("💬 Simple GenAI Text Generator")
prompt = st.text_area("Enter your prompt below:", "Once upon a time")
length = st.slider("Max words to generate", 10, 100, 30)

if st.button("Generate"):
    generator = load_model()
    set_seed(42)
    output = generator(prompt, max_length=length, num_return_sequences=1)
    st.subheader("Generated Text:")
    st.write(output[0]['generated_text'])
