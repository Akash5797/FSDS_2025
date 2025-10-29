import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Streamlit setup
st.set_page_config(page_title="NLP Text Processing", layout="centered")

# Light minimal styling (no colors)
st.markdown("""
    <style>
    h1 {
        text-align: center;
        color: #333333;
    }
    .button-row {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h2>NLP Text Processing App Created By Akash</h2>", unsafe_allow_html=True)

# Input text area
text = st.text_area("Enter your text here:", height=150, placeholder="Type or paste your text...")

# Initialize tools
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Centered buttons (default color)
st.markdown('<div class="button-row">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="small")

with col1:
    token_btn = st.button("Tokenization")
with col2:
    stem_btn = st.button("Stemming")
with col3:
    lemma_btn = st.button("Lemmatization")
with col4:
    wc_btn = st.button("WordCloud")

st.markdown('</div>', unsafe_allow_html=True)

# Backend logic
if token_btn:
    if text:
        tokens = word_tokenize(text)
        st.success("Tokens Generated:")
        st.write(tokens)
    else:
        st.warning("Please enter some text!")

elif stem_btn:
    if text:
        tokens = word_tokenize(text)
        stemmed = [ps.stem(w) for w in tokens]
        st.success("Stemming Completed:")
        st.write(stemmed)
    else:
        st.warning("Please enter some text!")

elif lemma_btn:
    if text:
        tokens = word_tokenize(text)
        lemmatized = [lemmatizer.lemmatize(w) for w in tokens]
        st.success("Lemmatization Completed:")
        st.write(lemmatized)
    else:
        st.warning("Please enter some text!")

elif wc_btn:
    if text:
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)
    else:
        st.warning("Please enter some text!")
