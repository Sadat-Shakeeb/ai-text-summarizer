# T5 AI Summarizer

A lightweight web application for abstractive text summarization, powered by a fine-tuned T5 model. The app is built with Streamlit and fetches model artifacts from the Hugging Face Hub so the repository only contains source code (no model weights).

Live demo: https://t5-aisummarizer.streamlit.app/  
Model on Hugging Face: https://huggingface.co/shakeeb08/t5-text-summarizer

---

## Overview

This project provides a user-friendly interface to generate concise or detailed summaries for conversational data and short-form text. The model was fine-tuned on conversational summarization data (SAMSum-style), which makes it especially effective on dialogues, chats, meeting transcripts, and emails.

Key capabilities:
- Abstractive summarization (T5)
- Two summary modes: Short and Detailed
- Fast inference with caching in Streamlit
- Deployed on Streamlit Cloud with model hosted on Hugging Face Hub

---

## Features

- Abstractive summarization using a fine-tuned T5 model
- Short and Detailed summary options
- Clean, minimal Streamlit UI for easy interaction
- Automatic download of model/tokenizer from Hugging Face on first run
- Optimized for dialogue-style inputs

---

## Model Details

- Architecture: T5 (Text-to-Text Transformer)
- Tokenizer: SentencePiece
- Fine-tuned dataset: Conversational summarization (SAMSum-style)
- Model hub: [shakeeb08/t5-text-summarizer](https://huggingface.co/shakeeb08/t5-text-summarizer)

---

## Repository Structure

```
ai-text-summarizer/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

Note: Model weights and tokenizer files are hosted on Hugging Face and are not included in this repository.

---

## Quick Start (Run locally)

1. Clone the repository
```bash
git clone https://github.com/Sadat-Shakeeb/ai-text-summarizer.git
cd ai-text-summarizer
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Launch the app
```bash
streamlit run app.py
```

The app will download the model and tokenizer from the Hugging Face Hub the first time it runs. If the model is private, set your Hugging Face token in the environment before running:

```bash
export HUGGINGFACE_HUB_TOKEN="hf_xxx"
```

---

## Usage

- Paste or type a dialogue, chat log, email, or short article into the text input.
- Select summary style:
  - Short — concise one-sentence overview or brief paragraph.
  - Detailed — longer, more informative summary that captures key points.
- Click the button to generate the summary; result will appear in the output panel.

Tips for best results:
- Provide clear speaker labels in conversations when possible.
- Break very long documents into sections and summarize individually.

---

## Deployment

The application is deployed on Streamlit Cloud:

- Live demo: https://t5-aisummarizer.streamlit.app/

Model artifacts (weights & tokenizer): hosted on Hugging Face Hub at [shakeeb08/t5-text-summarizer](https://huggingface.co/shakeeb08/t5-text-summarizer).

---

## Roadmap / Future Improvements

Potential enhancements:
- File upload support (TXT / PDF)
- Automatic language detection
- Upgrade to T5-base or T5-large for quality improvements
- Summary history, export options (CSV / TXT)
- UI/UX enhancements and usage analytics
- Batch summarization and API endpoint

---

## Contributing

Contributions, suggestions, and bug reports are welcome. To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Open a pull request describing your changes.

Please include tests or a short demo where applicable.

---

## License & Intended Use

This project is provided for educational and demonstration purposes. If you plan to use the model in production, evaluate model behavior carefully and review the license and model card on Hugging Face.

---

## Author

Sadat Shakeeb — Machine Learning & NLP Enthusiast  
- GitHub: https://github.com/Sadat-Shakeeb  
- Hugging Face: https://huggingface.co/shakeeb08

---
