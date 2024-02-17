import glob
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px
english_stopwords = stopwords.words('english')

file_paths = sorted(glob.glob('./diary/*.txt'))
dates_list = [list.strip(".txt").strip('./diary/') for list in file_paths]

analyzer = SentimentIntensityAnalyzer()
corpus = []
for file in file_paths:
    with open(file) as f_input:
        corpus.append(f_input.read())


negative_array = []
positive_array = []

for index, content in enumerate(corpus):        
    scores = analyzer.polarity_scores(content)
    negative_array.append(scores['neg'])
    positive_array.append(scores['pos'])


figure_pos = px.line(x=dates_list, y=positive_array, labels={"x": "Dates", "y": "Positive Sentiment"})
figure_neg = px.line(x=dates_list, y=negative_array, labels={"x": "Dates", "y": "Negative Sentiment"})

st.markdown("# Sentiment in Diary")
st.image('./images/mood.jpg')
st.markdown("## Positive Sentiment")
st.plotly_chart(figure_pos)
st.markdown("## Negative Sentiment")
st.plotly_chart(figure_neg)