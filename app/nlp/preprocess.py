import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

stop_words = set(stopwords.words("portuguese"))
stemmer = RSLPStemmer()

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zà-ú\s]", " ", text)
    tokens = text.split()
    tokens = [
        stemmer.stem(word)
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)
