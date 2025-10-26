from openai import OpenAI
import streamlit as st
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

openai_api_key = st.secrets["general"]["openai_api_key"]
client = OpenAI(api_key=openai_api_key)  # reads OPENAI_API_KEY from env

resp = client.chat.completions.create(
    model="gpt-5-nano",                 # or "gpt-4o", "gpt-4.1-mini"
    messages=[{"role":"user","content":"Plan a 1-day trip to Kyoto."}],
    max_tokens=60                   # tokens to generate
)
print(resp.choices[0].message.content)
