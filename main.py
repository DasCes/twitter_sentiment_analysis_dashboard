import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import schedule
import time

# Page setting
st.set_page_config(layout="centered", page_icon="Logo_of_Twitter.png",page_title="SenForWirn2023")
st.title("Sentiment analysis of last week's tweets", anchor=None, help=None)


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
data = pd.read_csv('data/all_at_21_05_2023.csv', index_col=[0])
data = data.head(10)

data['created_at'] = pd.to_datetime(data['created_at'])
start_date = datetime.strptime("2023-03-10 01:44:38+00:00", "%Y-%m-%d %H:%M:%S%z")
end_date = datetime.strptime("2023-03-17 01:44:38+00:00", "%Y-%m-%d %H:%M:%S%z")
mask = (data['created_at'] > start_date) & (data['created_at'] <= end_date)
data = data.loc[mask]
data.reset_index(drop=True, inplace=True)

tweets_of_week = {}
for i, x in enumerate(data.created_at):
    giorno = x.date().day
    if giorno in tweets_of_week:
        tweets_of_week[giorno] += 1
    else:
        tweets_of_week[giorno] = 1


data["Sommatoria"] = 1
sorted(tweets_of_week)
fig = px.bar(x=list(tweets_of_week.keys()), y=list(tweets_of_week.values()))
# fig = px.bar(data, x='created_at', y='Sommatoria')
fig.update_layout(xaxis_title="day", yaxis_title="number of tweets")
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")


st.header("Sentiment analysis by XML-roBERTa", anchor=None, help=None)
# per creare pie chart xml_roberta
score_for_xmlroberta_piechart = [0, 0, 0]
labels = ["negative", "neutral", "positive"]
for x in data.xlm_roberta_SCORE_numeric:
    score_for_xmlroberta_piechart[int(x)+1] += 1

fig = px.pie(names=labels, values=score_for_xmlroberta_piechart)
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")



st.header("Sentiment analysis by vader", anchor=None, help=None)
# per creare pie chart xml_roberta
score_for_vader_piechart = [0, 0, 0]
labels = ["negative", "neutral", "positive"]
for x in data.vader_SCORE_pnn_numeric:
    score_for_vader_piechart[int(x)+1] += 1

fig = px.pie(names=labels, values=score_for_vader_piechart)
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")




""" proviamo a stampre ogni n secondi """
WAIT_SECONDS = 5
def stampa_tempo_ogni_n():
    st.write(time.ctime())

schedule.every(WAIT_SECONDS).seconds.do(stampa_tempo_ogni_n)



while True:
        schedule.run_pending()
        time.sleep(1)