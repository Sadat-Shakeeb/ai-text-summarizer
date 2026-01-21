```md
# 📝 T5 AI Summarizer

A web-based **text summarization application** built using a fine-tuned **T5 Transformer model**, deployed live with **Streamlit Cloud** and hosted model artifacts on **Hugging Face Hub**.

🔗 **Live Demo:**  
👉 https://t5-aisummarizer.streamlit.app/

---

## 📌 Project Overview

This project provides an **abstractive text summarization system** capable of generating **short or detailed summaries** for:

- Conversations and dialogues (best performance)
- Chats, emails, meeting transcripts
- General text and short articles

The model is fine-tuned on conversational data and exposed through a clean, user-friendly Streamlit interface.

---

## 🚀 Features

- ✨ Abstractive text summarization using **T5**
- 🔄 Supports **Short** and **Detailed** summaries
- ⚡ Fast loading with Streamlit caching
- ☁️ Deployed live on **Streamlit Cloud**
- 📦 Model hosted on **Hugging Face Hub** (no large files in GitHub)
- 🧠 Optimized for conversational text (SAMSum-style data)

---

## 🧠 Model Details

- **Model Architecture:** T5 (Text-to-Text Transformer)
- **Task:** Abstractive Text Summarization
- **Tokenizer:** SentencePiece
- **Model Hosting:** Hugging Face Hub  
  👉 https://huggingface.co/shakeeb08/t5-text-summarizer

---

## 🏗️ System Architecture

```

User
↓
Streamlit Web App
↓
Hugging Face Transformers
↓
T5 Model (Hosted on Hugging Face Hub)

```

- **GitHub:** Source code only
- **Hugging Face Hub:** Model weights & tokenizer
- **Streamlit Cloud:** Live deployment

---

## 🖥️ User Interface

- Text input area for dialogue or text
- Summary style selector:
  - **Short** – concise overview
  - **Detailed** – more informative summary
- Output displayed in a clean, readable format

💡 *Best results are obtained with conversational or dialogue-style text.*

---

## 📂 Repository Structure

```

ai-text-summarizer/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

````

> ⚠️ Model files are intentionally **not included** in this repository.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **PyTorch**
- **Hugging Face Transformers**
- **SentencePiece**
- **Hugging Face Hub**

---

## ⚙️ Installation (Run Locally)

```bash
git clone https://github.com/Sadat-Shakeeb/ai-text-summarizer.git
cd ai-text-summarizer
pip install -r requirements.txt
streamlit run app.py
````

> The model will be downloaded automatically from Hugging Face Hub on first run.

---

## 🌐 Live Deployment

The application is deployed using **Streamlit Cloud**:

🔗 [https://t5-aisummarizer.streamlit.app/](https://t5-aisummarizer.streamlit.app/)

No authentication is required to use the app.

---

## 📈 Future Improvements

* File upload support (TXT / PDF)
* Automatic language detection
* Model upgrade (T5-base / T5-large)
* Summary history & export
* UI enhancements and analytics

---

## 👤 Author

**Sadat Shakeeb**
📌 Machine Learning & NLP Enthusiast

* GitHub: [https://github.com/Sadat-Shakeeb](https://github.com/Sadat-Shakeeb)
* Hugging Face: [https://huggingface.co/shakeeb08](https://huggingface.co/shakeeb08)

---

## 📄 License

This project is for educational and demonstration purposes.

```

---



Just tell me 👍
```
