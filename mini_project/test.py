import glob
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import pandas as pd
import plotly.express as px
english_stopwords = stopwords.words('english')

filepaths = sorted(glob.glob('./diary/*.txt'))
new_file_list = []
for file in filepaths:
    file = file.replace('./diary/', '').replace('.txt', '')
    new_file_list.append(file)


analyzer = SentimentIntensityAnalyzer()
print
corpus = []
for file in filepaths:
    with open(file) as f_input:
        corpus.append(f_input.read())

negative_array = []
positive_array = []

for index, content in enumerate(corpus):
    scores = analyzer.polarity_scores(content)
    negative_array.append(scores['neg'])
    positive_array.append(scores['pos'])

print(negative_array)
print(positive_array)