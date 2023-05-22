import streamlit as st
import pandas as pd
import plotly.express as px


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

for week_start, week_analysis in tweets_by_week.iterrows():
    current_week = []
    current_week.append(week_start.strftime('%Y-%m-%d'))
    vader_negative = week_analysis['vader_SCORE_pnn_numeric'].count(-1.0)
    current_week.append(vader_negative)

    vader_neutral = week_analysis['vader_SCORE_pnn_numeric'].count(0.0)
    current_week.append(vader_neutral)

    vader_positive = week_analysis['vader_SCORE_pnn_numeric'].count(1.0)
    current_week.append(vader_positive)
    df_list.append(current_week)
    # print(current_week)

    df = pd.DataFrame(df_list, columns=["weeks", "negative", "neutral", "positive"])



fig = px.bar(df, x="weeks", y=["negative", "neutral", "positive"], barmode='group', height=400)
st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig)