import streamlit as st
from textblob import TextBlob
import spacy
from spacy import displacy

# ---------------------------
# Load spaCy model
# ---------------------------
nlp = spacy.load("en_core_web_sm")

# ---------------------------
# NLP Functions
# ---------------------------
def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def extract_keywords(text):
    doc = nlp(text.lower())
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    freq = {}
    for word in keywords:
        freq[word] = freq.get(word, 0) + 1
    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return ", ".join([word for word, _ in sorted_keywords[:10]])

def word_count(text):
    return len(text.split())

def sentence_count(text):
    doc = nlp(text)
    return len(list(doc.sents))

def char_count(text):
    return len(text), len(text.replace(" ", ""))

def reading_time(text):
    words = word_count(text)
    time_min = words / 200
    return round(time_min, 2)

def most_frequent_word(text):
    doc = nlp(text.lower())
    words = [token.text for token in doc if token.is_alpha and not token.is_stop]
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    if not freq:
        return "No frequent words"
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[0][0]

def highlight_ner(text):
    doc = nlp(text)
    ents_html = displacy.render(doc, style="ent", page=True)
    return ents_html

# ---------------------------
# Streamlit App Layout
# ---------------------------
st.set_page_config(page_title="Professional Text Analyzer", layout="wide")

# ---------------------------
# Light Theme CSS
# ---------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffffff 0%, #f2f2f2 100%);
    color: #000000;
    font-family: 'Helvetica', sans-serif;
}
h1, h2, h3, h4, h5, h6 {
    color: #333333;
}
div.stButton > button:first-child {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    padding: 10px 25px;
    border-radius: 8px;
    border: none;
}
div.stButton > button:first-child:hover {
    background-color: #45a049;
}
textarea, .stTextInput>div>input {
    background-color: #f9f9f9;
    color: #000000;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# App Title
# ---------------------------
st.title("NLP-Powered Text Insights")
st.markdown("Analyze text: sentiment, keywords, word count, reading time, sentence count, most frequent word, and NER visualization.")

tab1, tab2 = st.tabs(["Text Analysis", "NER Visualization"])

# ---------------------------
# TAB 1: Text Analysis
# ---------------------------
with tab1:
    uploaded_file = st.file_uploader("Upload a .txt file (optional)", type=["txt"])
    if uploaded_file:
        text_data = uploaded_file.read().decode("utf-8")
    else:
        text_data = st.text_area("Enter your text here:", height=250)

    if st.button("Analyze Text"):
        if not text_data or text_data.strip() == "":
            st.warning("Please enter text or upload a file!")
        else:
            st.subheader("1.Sentiment Analysis")
            st.write(analyze_sentiment(text_data))

            st.subheader("2.Top Keywords")
            st.write(extract_keywords(text_data))

            st.subheader("3.Word Count")
            st.write(word_count(text_data))

            st.subheader("4.Sentence Count")
            st.write(sentence_count(text_data))

            st.subheader("5.Character Count (with spaces / without)")
            total_chars, chars_no_space = char_count(text_data)
            st.write(f"{total_chars} / {chars_no_space}")

            st.subheader("⏱6.Estimated Reading Time (minutes)")
            st.write(reading_time(text_data))

            st.subheader("7.Most Frequent Word")
            st.write(most_frequent_word(text_data))

# ---------------------------
# TAB 2: NER Visualization
# ---------------------------
with tab2:
    ner_text = st.text_area("Enter text for NER highlighting:", height=250)
    if st.button("Show Named Entities"):
        if ner_text.strip() == "":
            st.warning("Please enter text for NER visualization!")
        else:
            st.subheader("Named Entity Recognition (NER)")
            st.components.v1.html(highlight_ner(ner_text), height=400, scrolling=True)
