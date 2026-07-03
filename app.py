"""
FAQ Chatbot — Streamlit App
Matches user questions to the closest FAQ using Sentence-BERT embeddings
and cosine similarity, and displays the corresponding answer.
"""

import streamlit as st
from sentence_transformers import SentenceTransformer, util
from faq_data import FAQ_DATA

# ----------------------------------------------------------------------
# Page config
# ----------------------------------------------------------------------
st.set_page_config(page_title="FAQ Chatbot", page_icon="💬", layout="centered")

st.title("💬 FAQ Chatbot")
st.caption("Ask a question and I'll match it to the closest FAQ using semantic similarity.")

# ----------------------------------------------------------------------
# Load model + precompute FAQ embeddings (cached so it only runs once)
# ----------------------------------------------------------------------
@st.cache_resource(show_spinner="Loading model...")
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


@st.cache_resource(show_spinner="Indexing FAQs...")
def build_faq_index(_model):
    questions = [item["question"] for item in FAQ_DATA]
    embeddings = _model.encode(questions, convert_to_tensor=True)
    return embeddings


model = load_model()
faq_embeddings = build_faq_index(model)

# ----------------------------------------------------------------------
# Sidebar settings
# ----------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    threshold = st.slider(
        "Confidence threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.45,
        step=0.05,
        help="Minimum similarity score required to trust a match. "
             "Lower = more answers but riskier matches. Higher = stricter matching.",
    )
    show_score = st.checkbox("Show match confidence", value=True)
    st.divider()
    st.markdown(f"**Total FAQs loaded:** {len(FAQ_DATA)}")
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.markdown("Built with `sentence-transformers` + `streamlit`.")

# ----------------------------------------------------------------------
# Matching function
# ----------------------------------------------------------------------
def get_answer(user_query: str, threshold: float = 0.45):
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, faq_embeddings)[0]
    best_idx = int(scores.argmax())
    best_score = float(scores[best_idx])

    if best_score < threshold:
        return (
            "Sorry, I couldn't find a confident answer to that. "
            "Try rephrasing your question, or contact support@example.com.",
            best_score,
            None,
        )
    return FAQ_DATA[best_idx]["answer"], best_score, FAQ_DATA[best_idx]["question"]

# ----------------------------------------------------------------------
# Chat state
# ----------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! 👋 Ask me anything about your account, orders, payments, or support."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ----------------------------------------------------------------------
# Chat input
# ----------------------------------------------------------------------
user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    answer, score, matched_question = get_answer(user_input, threshold)

    with st.chat_message("assistant"):
        st.write(answer)
        if show_score:
            if matched_question:
                st.caption(f"Matched FAQ: _{matched_question}_ · confidence: {score:.2f}")
            else:
                st.caption(f"confidence: {score:.2f}")

    st.session_state.messages.append({"role": "assistant", "content": answer})
