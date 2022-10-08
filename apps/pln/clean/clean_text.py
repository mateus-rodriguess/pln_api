import re

def clean_text(text):
    text = str(text)
    text = re.sub(r"@[A-Za-z0-9]+", ' ', text)
    text = re.sub(r"https?://[A-Za-z0-9./]+", ' ', text)
    text = re.sub(r"[^a-zA-Z.!?]", ' ', text)
    text = re.sub(r" +", ' ', text)
    return text


def clean_text2(text, nlp):
    text = text.lower()
    # document = nlp(text)
    # words = []
    # for token in document:
    #     words.append(token.text)

    # words = [word for word in words]
    # words = ' '.join([str(element) for element in words])

    return text
    #return words
