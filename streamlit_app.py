import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime, timedelta


# df = pd.DataFrame(
#     [["Product A", 5.6, 7.8, 5], ["Product B", 5.8, 7.2, 4.9]],
#     columns=["weeks", "negative", "neutral", "positive"]
# )


data = pd.read_csv('data/all_at_21_05_2023.csv', index_col=[0])
data['created_at'] = pd.to_datetime(data['created_at'])
data.set_index("created_at", inplace=True)
# print(data)
tweets_by_week = data.resample('W').apply(list)

df_list = []

for end_week_day, week_analysis in tweets_by_week.iterrows():
    current_week = []

    # tutte ste righe per far sì che la label si "12-19" dove 12 è il primo giorno della settimana in esame e 19 è l'ultimo
    endDay_week_string = end_week_day.strftime('%Y-%m-%d')
    date = datetime.strptime(endDay_week_string, '%Y-%m-%d')
    week_before = date - timedelta(weeks=1)
    firstDay_week_string = week_before.strftime('%Y-%m-%d')
    endDay_week_string = endDay_week_string[-2:]
    firstDay_week_string = firstDay_week_string[-2:]
    week_label = firstDay_week_string + "-" + endDay_week_string

    current_week.append(week_label)


    vader_negative = week_analysis['vader_SCORE_pnn_numeric'].count(-1.0)
    current_week.append(vader_negative)

    vader_neutral = week_analysis['vader_SCORE_pnn_numeric'].count(0.0)
    current_week.append(vader_neutral)

    vader_positive = week_analysis['vader_SCORE_pnn_numeric'].count(1.0)
    current_week.append(vader_positive)
    df_list.append(current_week)

    df = pd.DataFrame(df_list, columns=["weeks", "negative", "neutral", "positive"])



fig = px.bar(df, x="weeks", y=["negative", "neutral", "positive"], barmode='group', height=400)
st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig)