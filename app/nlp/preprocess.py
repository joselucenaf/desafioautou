import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

stop_words = set(stopwords.words("portuguese"))
stemmer = RSLPStemmer()

def preprocess_text(text: str) -> str:
    # 1. lowercase
    text = text.lower()

    # 2. remover caracteres especiais
    text = re.sub(r"[^a-zà-ú\s]", " ", text)

    # 3. tokenização simples
    tokens = text.split()

    # 4. remover stopwords e aplicar stemming
    tokens = [
        stemmer.stem(word)
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)
