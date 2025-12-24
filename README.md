# Basic-NLP-Plug-in-to-add-Stopwords
Add Custom Stopwords in your NLTK for text Processing

install nltk before running using: 'pip install nltk' in terminal


run and refer example.py to see how to add custom stopwords

ADD THIS FUNCTION IN YOUR NLP PIPELINE

def preprocess(text, stopwords_plugin):
    return [
        word for word in text.lower().split()
        if not stopwords_plugin.is_stopword(word)
    ]
