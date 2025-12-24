import json
import os
from nltk.corpus import stopwords

class CustomStopwords:
    def __init__(self, language="english", storage_path="custom_stopwords.json"):
        self.language = language
        self.storage_path = storage_path

        if not os.path.exists(self.storage_path):
            self._initialize_storage()

        self._load_custom_stopwords()

    def _initialize_storage(self):
        with open(self.storage_path, "w") as f:
            json.dump({}, f)

    def _load_custom_stopwords(self):
        with open(self.storage_path, "r") as f:
            data = json.load(f)

        self.custom_stopwords = set(data.get(self.language, []))
        self.base_stopwords = set(stopwords.words(self.language))

    def add(self, words):
        if isinstance(words, str):
            words = [words]

        self.custom_stopwords.update(word.lower() for word in words)
        self._save()

    def remove(self, words):
        if isinstance(words, str):
            words = [words]

        for word in words:
            self.custom_stopwords.discard(word.lower())

        self._save()

    def get_all(self):
        return self.base_stopwords.union(self.custom_stopwords)

    def is_stopword(self, word):
        return word.lower() in self.get_all()

    def _save(self):
        with open(self.storage_path, "r") as f:
            data = json.load(f)

        data[self.language] = sorted(self.custom_stopwords)

        with open(self.storage_path, "w") as f:
            json.dump(data, f, indent=4)
