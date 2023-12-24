import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
import glob

analyzer = SentimentIntensityAnalyzer()

full_diary = glob.glob('diary/*.txt')

data_diary = {}
xx = []

for date in full_diary:
    with open(date, 'r', encoding="utf8") as file:
        diary = file.read()
    analysis = analyzer.polarity_scores(diary)
    date = date[6:-4]
    xx.append(date)
    data_diary[date] = analysis

pos_y = [data_diary[i]['pos'] for i in data_diary]
neg_y = [data_diary[i]['neg'] for i in data_diary]

st.title('Diary Tone')

st.subheader('Positivity')
pos_figure = px.line(x=xx, y=pos_y,
                     labels={'x': f'Date', 'y': f'Positivity'})
st.plotly_chart(pos_figure)

st.subheader('Negativity')
neg_figure = px.line(x=xx, y=neg_y,
                     labels={'x': f'Date', 'y': f'Negativity'})
st.plotly_chart(neg_figure)

