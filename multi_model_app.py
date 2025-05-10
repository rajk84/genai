import streamlit as st
from transformers import pipeline, set_seed

@st.cache_resource
def load_pipeline(task):
    if task == "Text Generation":
        return pipeline("text-generation", model="gpt2")
    elif task == "Summarization":
        return pipeline("summarization", model="t5-small")
    elif task == "Sentiment Analysis":
        return pipeline("sentiment-analysis")
    else:
        raise ValueError("Invalid task")

# UI
st.title("🧠 GenAI Model Playground")
task = st.selectbox("Choose a task", ["Text Generation", "Summarization", "Sentiment Analysis"])

user_input = st.text_area("Enter your text:", "Agentic AI will change how we interact with machines.")

if st.button("Run"):
    pipe = load_pipeline(task)

    if task == "Text Generation":
        set_seed(42)
        result = pipe(user_input, max_length=50, num_return_sequences=1)
        st.subheader("Generated Text:")
        st.write(result[0]['generated_text'])

    elif task == "Summarization":
        result = pipe(user_input, max_length=50, min_length=10, do_sample=False)
        st.subheader("Summary:")
        st.write(result[0]['summary_text'])

    elif task == "Sentiment Analysis":
        result = pipe(user_input)
        label = result[0]['label']
        score = round(result[0]['score'], 3)
        st.subheader("Sentiment:")
        st.write(f"{label} ({score})")
