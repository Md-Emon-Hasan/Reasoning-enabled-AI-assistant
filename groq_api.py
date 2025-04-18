import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq
import re

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY is missing in .env file.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

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
    # Try to extract the <think> tag content
    thought_match = re.search(r"<think>(.*?)</think>", content, re.DOTALL)
    if thought_match:
        thought = thought_match.group(1).strip()
        answer = content.replace(thought_match.group(0), "").strip()
    else:
        # If no <think> tag is found, use a default thinking message
        thought = "🤔 Model did not provide explicit reasoning."
        answer = content.strip()
    return thought, answer

# Get response from model
def generate_response(description: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": description}
            ],
            temperature=0.7,
            max_tokens=1200,
            top_p=1,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit UI config
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

# Input box
prompt = st.chat_input("Type your coding question here...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            output = generate_response(prompt)
            thinking, answer = parse_thinking_output(output)

            # Show thought process and final answer
            st.markdown("### 🔍 Thinking...")
            st.markdown(thinking)
            st.markdown("---")

            st.markdown("### ✅ Final Answer")
            st.markdown(answer)

    # Save assistant response
    full_response = f"### 🔍 Thought Process\n{thinking}\n\n### ✅ Final Answer\n{answer}"
    st.session_state.messages.append({"role": "assistant", "content": full_response})