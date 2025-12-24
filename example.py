import nltk
from custom_stopwords import CustomStopwords

nltk.download("stopwords")

# Initialize plugin
stopword_plugin = CustomStopwords(language="english")

# Add domain-specific stopwords
stopword_plugin.add(["api", "server", "client", "request"])

# Sample text
text = "The client sends a request to the API server"
tokens = text.lower().split()

# Filter stopwords
filtered = [w for w in tokens if not stopword_plugin.is_stopword(w)]

print(filtered)
