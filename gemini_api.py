import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import re

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GEMINI_API_KEY:
    st.error("❌ GOOGLE_API_KEY is missing in .env file.")
    st.stop()

# Initialize Gemini client
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-2.0-flash-thinking-exp-01-21")

# System prompt for consistent expert behavior
SYSTEM_PROMPT = """
You are an expert Python developer and software architect with deep knowledge in writing production-quality, clean, modular, and well-documented code.

Your job is to:
- Understand the user's coding task or error
- Think step-by-step before writing any code
- Follow best practices: PEP8, DRY, modularity, and docstrings
- Add detailed in-code comments for beginners to understand
- Suggest improvements or alternatives if necessary
- Avoid unnecessary complexity and dependencies

Always structure your output like this:
<think>
Step-by-step explanation goes here.
</think>
Final optimized code follows the explanation.
"""

# Parse thinking and final answer
def parse_thinking_output(content: str) -> tuple:
    thought_match = re.search(r"<think>(.*?)</think>", content, re.DOTALL)
    if thought_match:
        thought = thought_match.group(1).strip()
        answer = content.replace(thought_match.group(0), "").strip()
    else:
        thought = "🤔 Model did not provide explicit reasoning."
        answer = content.strip()
    return thought, answer

# Get response from Gemini
def generate_response(user_input: str) -> str:
    try:
        chat = model.start_chat(history=[
            {"role": "user", "parts": [SYSTEM_PROMPT]},
        ])
        response = chat.send_message(user_input)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Coding Assistant", layout="centered")
st.title("💻 AI Powered Python Coding Assistant")
st.caption("Made by Emon Hasan")
st.write("📝 Ask me anything about Python coding!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
prompt = st.chat_input("Type your coding question here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt)
            thinking, answer = parse_thinking_output(response)

            st.markdown("### 🔍 Thinking...")
            st.markdown(thinking)
            st.markdown("---")
            st.markdown("### ✅ Final Answer")
            st.markdown(answer)

    full_response = f"### 🔍 Thought Process\n{thinking}\n\n### ✅ Final Answer\n{answer}"
    st.session_state.messages.append({"role": "assistant", "content": full_response})