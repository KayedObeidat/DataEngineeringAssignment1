import re
import nltk
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from spellchecker import SpellChecker
import matplotlib.pyplot as plt
from pymongo import MongoClient  
import spacy
from wordcloud import WordCloud  
from tqdm import tqdm  

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

nlp = spacy.load("en_core_web_sm")

client = MongoClient("mongodb://localhost:27017")  
DB = client['UsersAPI']

collection = DB['Users']

def process_text(text):
    words = re.findall(r'\w+', text.lower())  
    return words

def get_most_frequent_words(documents, num=10):
    all_words = []
    for doc in documents:
        text = doc['address'] + " " + doc['name'] + " " + doc['email'] 
        words = process_text(text)
        all_words.extend(words)
    word_counts = Counter(all_words)
    return word_counts.most_common(num)

def plot_word_frequency(word_counts):
    words, counts = zip(*word_counts)
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xticks(rotation=45)
    plt.title("Top 10 Most Frequent Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.show()

def plot_word_cloud(word_counts):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_counts)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud for Most Frequent Words")
    plt.show()

def find_spelling_mistakes(documents):
    spell = SpellChecker()
    misspelled = []
    for doc in documents:
        text = doc['address'] + " " + doc['name'] + " " + doc['email']
        words = process_text(text)
        misspelled.extend(spell.unknown(words))
    return misspelled

def remove_stopwords_and_punctuation(words):
    cleaned_words = [word for word in words if word not in stop_words and len(word) > 1]
    return cleaned_words

def lemmatize_words(words):
    doc = nlp(" ".join(words))
    return [token.lemma_ for token in doc]

documents = list(collection.find())

print("Starting Data Profiling...")

all_words = []
for doc in documents:
    text = doc['address'] + " " + doc['name'] + " " + doc['email']
    words = process_text(text)
    all_words.extend(words)

word_counts = Counter(all_words)

most_frequent_words = word_counts.most_common(10)
print("10 Most Frequent Words:", most_frequent_words)

plot_word_frequency(most_frequent_words)

plot_word_cloud(word_counts)

misspelled_words = find_spelling_mistakes(documents)
print("Spelling Mistakes:", misspelled_words)

print("Process Completed!")
