import streamlit as st
from transformers import pipeline

st.title("🧙‍♂️ Story Bot")
st.write("Tell me a topic, and I will generate a story for you!")

story_gen = pipeline("text-generation", model="gpt2")

topic = st.text_input("Enter a topic:")

if st.button("Generate Story"):
    if topic:
        result = story_gen(topic, max_length=100, num_return_sequences=1)
        st.write(result[0]['generated_text'])
    else:
        st.warning("Please enter a topic.")