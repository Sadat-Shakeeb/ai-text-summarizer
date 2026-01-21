import streamlit as st
import re
import torch
from transformers import T5ForConditionalGeneration, T5TokenizerFast

# =========================
# Page config
# =========================
st.set_page_config(
    page_title="Text Summarization",
    page_icon="📝",
    layout="centered"
)

# =========================
# Sidebar
# =========================
st.sidebar.title("🧠 About")
st.sidebar.markdown(
    """
    **Text Summarization App**

    This app uses a fine-tuned **T5 Transformer**
    to generate concise or detailed summaries.

    **Task:** Abstractive Summarization  
    **Best for:** Conversations & chats  
    """
)

# =========================
# Load model (from HF Hub)
# =========================
@st.cache_resource
def load_model():
    MODEL_ID = "shakeeb08/t5-text-summarizer"


    tokenizer = T5TokenizerFast.from_pretrained(MODEL_ID)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_ID)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    model.eval()

    return tokenizer, model, device


tokenizer, model, device = load_model()

# =========================
# Helpers
# =========================
def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def summarize_text(text: str, style: str) -> str:
    text = "summarize: " + clean_text(text)

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).to(device)

    if style == "Short":
        max_len, min_len = 120, 30
    else:
        max_len, min_len = 200, 60

    with torch.no_grad():
        output_ids = model.generate(
            inputs["input_ids"],
            max_length=max_len,
            min_length=min_len,
            num_beams=6,
            length_penalty=1.2,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# =========================
# UI
# =========================
st.markdown(
    "<h1 style='text-align:center;'>📝 Text Summarization</h1>",
    unsafe_allow_html=True
)

st.info(
    "💡 Best results for conversations, chats, or dialogue-style text. "
    "General text is also supported."
)

text_input = st.text_area(
    "Input Text",
    height=220,
    placeholder="Paste conversation or text here..."
)

summary_style = st.selectbox(
    "Summary Style",
    ["Short", "Detailed"]
)

if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize_text(text_input, summary_style)

        st.text_area(
            "Generated Summary",
            value=summary,
            height=150,
            label_visibility="collapsed"
        )

st.markdown("---")
st.caption("Powered by T5 • Streamlit • Hugging Face")
