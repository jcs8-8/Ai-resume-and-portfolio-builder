from transformers import pipeline
import streamlit as st
from config.huggingface_config import MODEL_NAME, HF_API_KEY

@st.cache_resource
def load_generator():
    return pipeline(
        task="text2text-generation",   # ✅ CORRECT FOR T5
        model=MODEL_NAME,
        tokenizer=MODEL_NAME,
        token=HF_API_KEY,
        device=-1  # CPU
    )
