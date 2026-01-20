import os
from dotenv import load_dotenv

load_dotenv()

# 🔑 Hugging Face Token
HF_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# 🤖 Model name (REQUIRED)
MODEL_NAME = "google/flan-t5-base"

if HF_API_KEY is None:
    raise ValueError(
        "Hugging Face API token not found. "
        "Please set HUGGINGFACEHUB_API_TOKEN in .env"
    )
