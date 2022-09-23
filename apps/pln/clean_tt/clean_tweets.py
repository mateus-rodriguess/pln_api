import re

from bs4 import BeautifulSoup


def clean_texts(text):
    text = str(text)
    #text = BeautifulSoup(str(text), 'lxml').get_text()
    text = re.sub(r"@[A-Za-z0-9]+", ' ', text)
    text = re.sub(r"https?://[A-Za-z0-9./]+", ' ', text)
    text = re.sub(r"[^a-zA-Z.!?]", ' ', text)
    text = re.sub(r" +", ' ', text)
    return text


def clean_texts2(text, nlp):
    text = text.lower()
    # document = nlp(text)
    # words = []
    # for token in document:
    #     words.append(token.text)

    # words = [word for word in words]
    # words = ' '.join([str(element) for element in words])

    return text
    #eturn words
