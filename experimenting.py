import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import schedule
import time


data = pd.read_csv('data/all_at_21_05_2023.csv', index_col=[0])
# data = data.head(1000)
data['created_at'] = pd.to_datetime(data['created_at'])

data.set_index("created_at", inplace=True)
# print(data)
tweets_by_week = data.resample('W').apply(list)


for week_start, week_analysis in tweets_by_week.iterrows():
    vader_negative = week_analysis['vader_SCORE_pnn_numeric'].count(-1.0)
    vader_neutral = week_analysis['vader_SCORE_pnn_numeric'].count(0.0)
    vader_positive = week_analysis['vader_SCORE_pnn_numeric'].count(1.0)

    print(week_start, len(week_analysis['text']), vader_negative, vader_neutral, vader_positive)

