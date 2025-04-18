# 📁 Project Name: `AI-Powered-Python-Coding-Assistant-with-Reasoning-feature`
![Image](https://github.com/user-attachments/assets/c2c50425-e120-4a0d-826f-7aff9c12acf2)
---

## 💡 Overview

**AI Coding Assistant** is a developer-friendly tool that uses cutting-edge LLMs — **Gemini** and **Groq (DeepSeek-LLaMA)** — to help users debug, generate, and optimize Python code. It thinks step-by-step and outputs clean, modular, and well-commented Python code while explaining the logic behind it.

---

## 🎯 Features

- 🧠 Expert-level system prompt with thought-out reasoning
- 💬 Natural language interface using Streamlit chat UI
- 🤖 Supports both **Gemini 2.0 Flash** and **DeepSeek LLaMA 70B**
- 📝 Step-by-step `<think>` explanations and final code answers
- ♻️ Persistent chat history using `st.session_state`
- ⚠️ Clear API key handling using `.env`
- 💡 Beginner-friendly output with in-code comments

---

## 🛠️ Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| UI           | Streamlit            |
| LLM (Option 1) | Google Gemini API     |
| LLM (Option 2) | Groq DeepSeek-LLaMA  |
| Env Manager  | python-dotenv        |
| Language     | Python 3             |

---

## 🚀 Installation

```bash
git clone https://github.com/Md-Emon-Hasan/AI-Coding-Assistant.git
cd AI-Coding-Assistant
pip install -r requirements.txt
```

---

## 🔐 .env File Setup

Create a `.env` file in your root folder:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🧪 Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

- User types a Python-related question or error
- The assistant thinks step-by-step within `<think>` tags
- Outputs a clean, optimized code block
- Both Gemini and Groq models are integrated (one active per app)

---

## 📂 File Structure

```
AI-Coding-Assistant/
├── .env
├── app_gemini.py     # Gemini-based assistant
├── app_groq.py       # Groq (DeepSeek) based assistant
├── requirements.txt
└── README.md
```

---

## 📦 requirements.txt

```txt
streamlit
python-dotenv
google-generativeai
groq
```

---

## 📸 Screenshots

| Gemini | Groq |
|--------|------|
| ![Gemini Screenshot](link-to-gemini-screenshot) | ![Groq Screenshot](link-to-groq-screenshot) |

---

## 📬 Contact & Socials

Made with ❤️ by **Md Emon Hasan**

- 📧 **Email:** [iconicemon01@gmail.com](mailto:iconicemon01@gmail.com)
- 💬 **WhatsApp:** [Click to Chat](https://wa.me/8801834363533)
- 💻 **GitHub:** [Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)
- 🔗 **LinkedIn:** [Md Emon Hasan](https://www.linkedin.com/in/md-emon-hasan)
- 📘 **Facebook:** [Md Emon Hasan](https://www.facebook.com/mdemon.hasan2001/)

---

## 🧠 License

This project is open-source under the [MIT License](LICENSE).

---

## 🌟 Star This Repo

If this project helped you, please consider giving it a ⭐ on GitHub. It helps a lot!
