# 💬 FAQ Chatbot

A chatbot that answers user questions by matching them to the most similar FAQ using
Sentence-BERT embeddings and cosine similarity. Built with `sentence-transformers` and
`streamlit`.
https://faqchatbot-kqbvmtywz8hhr9ymaef8n7.streamlit.app/

## How it works

1. **FAQ data** — stored in `faq_data.py` as a list of `{question, answer}` pairs.
2. **Preprocessing / embedding** — each FAQ question is encoded into a vector using the
   pretrained `all-MiniLM-L6-v2` Sentence-BERT model (this happens once, cached).
3. **Matching** — a user's question is encoded the same way, then compared to every FAQ
   embedding using cosine similarity. The closest match above a confidence threshold is
   returned as the answer.
4. **UI** — a simple chat interface built with Streamlit's `st.chat_message` /
   `st.chat_input` components.

## Project structure

```
faq_chatbot/
├── app.py            # Streamlit app (UI + matching logic)
├── faq_data.py        # Your FAQ dataset (edit this to change topic/product)
├── requirements.txt   # Python dependencies
├── .gitignore
└── README.md
```

## Run locally

```bash
# 1. Clone your repo
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push this folder to a **public GitHub repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: FAQ chatbot"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main
   ```
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **"New app"**, select your repo, branch (`main`), and main file (`app.py`).
4. Click **"Deploy"**. Streamlit Cloud will install `requirements.txt` automatically and
   host your app at a public URL (e.g. `https://<your-app>.streamlit.app`).

> First load will take ~30–60 seconds while the Sentence-BERT model downloads — this is
> normal and only happens once per app restart, thanks to `@st.cache_resource`.

## Customizing for your own product/topic

Open `faq_data.py` and edit the `FAQ_DATA` list — just keep the same structure:

```python
FAQ_DATA = [
    {"question": "Your question here?", "answer": "Your answer here."},
    ...
]
```

No retraining is needed — the app re-embeds your FAQs automatically on startup.

## Tuning match quality

In the sidebar, adjust the **confidence threshold** slider:
- Lower it if the bot says "I couldn't find a confident answer" too often.
- Raise it if it's giving wrong/loose matches too confidently.

## Tech stack

- [Streamlit](https://streamlit.io/) — chat UI
- [sentence-transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`) — semantic embeddings
- Cosine similarity — matching metric
