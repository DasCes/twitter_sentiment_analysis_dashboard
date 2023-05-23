import inspect
import textwrap
import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime, timedelta

import streamlit as st

# data
data = pd.read_csv('data/all_at_21_05_2023.csv', index_col=[0])

# dati del dataset completo divisi per settimana
data['created_at'] = pd.to_datetime(data['created_at'])

# create df of last month
end_date = data['created_at'].max().date()  # Get the maximum date in the 'created_at' column
start_date = end_date - timedelta(days=30)  # Subtract 30 days from the end date
lastMonth_data = data[(data['created_at'].dt.date >= start_date) & (data['created_at'].dt.date <= end_date)]
lastMonth_data.set_index("created_at", inplace=True)
tweets_month = lastMonth_data.resample('D').apply(list)


end_date = data['created_at'].max().date()  # Get the maximum date in the 'created_at' column
start_date = end_date - timedelta(days=6)  # Subtract 30 days from the end date
lastWeek_data = data[(data['created_at'].dt.date >= start_date) & (data['created_at'].dt.date <= end_date)]
lastWeek_data.set_index("created_at", inplace=True)
tweets_week = lastWeek_data.resample('D').apply(list)


# create df complete divided by weeks
data.set_index("created_at", inplace=True)
tweets_by_week = data.resample('W').apply(list)







df_list = []
custom_labels = []


def main():


    with st.sidebar:
        st.header("Configuration")

        data_size = st.radio(
            "Seleziona il dataset",
            ('Complete dataset', 'last month', 'last week')
        )

        st.sidebar.markdown(" ")
        st.sidebar.markdown(" ")

        analysis_type = ("sentiment analysis", "topic analysis")
        analysis_type_selected = st.selectbox(
            label="Seleziona il tipo di analisi",
            options=analysis_type,
        )



        if analysis_type_selected == "sentiment analysis":
            sentiment_model_selected = st.radio(
                "which model?",
                ('vader', 'xlm_roBERTa')
            )
            # st.caption(
            #     """A lato viene mostrata le sentiment analysis prodotte da i modelli "vader" e "xlm roBERTa" """
            # )
        if analysis_type_selected == "topic analysis":
            st.caption(
                """A lato viene mostrata la topic analysis prodotta da "Bertopic model" """
            )


    if analysis_type_selected == "sentiment analysis":

            if data_size == "Complete dataset" and sentiment_model_selected == "vader":
                st.title("Sentiment analysis on complete dataset", anchor=None, help=None)
                df_list = []
                custom_labels = []
                for end_week_day, week_analysis in tweets_by_week.iterrows():
                    current_week = []
                    # tutte ste righe per far sì che la label si "12-19" dove 12 è il primo giorno della settimana in esame e 19 è l'ultimo
                    endDay_week_string = end_week_day.strftime('%Y-%m-%d')
                    date = datetime.strptime(endDay_week_string, '%Y-%m-%d')
                    week_before = date - timedelta(weeks=1)
                    firstDay_week_string = week_before.strftime('%Y-%m-%d')
                    endDay_week_string = endDay_week_string[-2:]
                    firstDay_week_string = firstDay_week_string[-2:]
                    month = week_before.strftime('%b')

                    week_label = month + " " + firstDay_week_string + "-" + endDay_week_string

                    print(week_label)
                    custom_labels.append(week_label)
                    current_week.append(end_week_day)

                    vader_negative = week_analysis['vader_SCORE_pnn_numeric'].count(-1.0)
                    current_week.append(vader_negative)

                    vader_neutral = week_analysis['vader_SCORE_pnn_numeric'].count(0.0)
                    current_week.append(vader_neutral)

                    vader_positive = week_analysis['vader_SCORE_pnn_numeric'].count(1.0)
                    current_week.append(vader_positive)
                    df_list.append(current_week)

                df = pd.DataFrame(df_list, columns=["weeks", "negative", "neutral", "positive"])
                st.subheader('vader sentiment analysis')
                fig = px.bar(df, x="weeks", y=["negative", "neutral", "positive"], barmode='group', height=400)
                fig.update_xaxes(ticktext=custom_labels, tickvals=df['weeks'])
                st.plotly_chart(fig)

            if data_size == "Complete dataset" and sentiment_model_selected == "xlm_roBERTa":
                st.title("Sentiment analysis on complete dataset", anchor=None, help=None)
                df_list = []
                custom_labels = []
                for end_week_day, week_analysis in tweets_by_week.iterrows():
                    current_week = []
                    # tutte ste righe per far sì che la label si "12-19" dove 12 è il primo giorno della settimana in esame e 19 è l'ultimo
                    endDay_week_string = end_week_day.strftime('%Y-%m-%d')
                    date = datetime.strptime(endDay_week_string, '%Y-%m-%d')
                    week_before = date - timedelta(weeks=1)
                    firstDay_week_string = week_before.strftime('%Y-%m-%d')
                    endDay_week_string = endDay_week_string[-2:]
                    firstDay_week_string = firstDay_week_string[-2:]
                    month = week_before.strftime('%b')

                    week_label = month + " " + firstDay_week_string + "-" + endDay_week_string

                    print(week_label)
                    custom_labels.append(week_label)
                    current_week.append(end_week_day)

                    vader_negative = week_analysis['xlm_roberta_SCORE_numeric'].count(-1.0)
                    current_week.append(vader_negative)

                    vader_neutral = week_analysis['xlm_roberta_SCORE_numeric'].count(0.0)
                    current_week.append(vader_neutral)

                    vader_positive = week_analysis['xlm_roberta_SCORE_numeric'].count(1.0)
                    current_week.append(vader_positive)
                    df_list.append(current_week)

                df = pd.DataFrame(df_list, columns=["weeks", "negative", "neutral", "positive"])
                st.subheader('xlm sentiment analysis')
                fig = px.bar(df, x="weeks", y=["negative", "neutral", "positive"], barmode='group', height=400)
                fig.update_xaxes(ticktext=custom_labels, tickvals=df['weeks'])
                st.plotly_chart(fig)

            if data_size == "last month" and sentiment_model_selected == "xlm_roBERTa":
                st.title("Sentiment analysis on last month dataset", anchor=None, help=None)
                df_list = []
                for day, day_analysis in tweets_month.iterrows():
                    current_day = []
                    current_day.append(str(day))
                    vader_negative = day_analysis['xlm_roberta_SCORE_numeric'].count(-1.0)
                    current_day.append(vader_negative)

                    vader_neutral = day_analysis['xlm_roberta_SCORE_numeric'].count(0.0)
                    current_day.append(vader_neutral)

                    vader_positive = day_analysis['xlm_roberta_SCORE_numeric'].count(1.0)
                    current_day.append(vader_positive)
                    df_list.append(current_day)

                df = pd.DataFrame(df_list, columns=["days", "negative", "neutral", "positive"])
                st.subheader('xlm sentiment analysis')
                fig = px.bar(df, x="days", y=["negative", "neutral", "positive"], barmode='group', height=400)
                # fig.update_xaxes(ticktext=custom_labels, tickvals=df['weeks'])
                st.plotly_chart(fig)

            if data_size == "last month" and sentiment_model_selected == "vader":
                st.title("Sentiment analysis on last month dataset", anchor=None, help=None)
                df_list = []
                for day, day_analysis in tweets_month.iterrows():
                    current_day = []
                    current_day.append(str(day))
                    vader_negative = day_analysis['vader_SCORE_pnn_numeric'].count(-1.0)
                    current_day.append(vader_negative)

                    vader_neutral = day_analysis['vader_SCORE_pnn_numeric'].count(0.0)
                    current_day.append(vader_neutral)

                    vader_positive = day_analysis['vader_SCORE_pnn_numeric'].count(1.0)
                    current_day.append(vader_positive)
                    df_list.append(current_day)

                df = pd.DataFrame(df_list, columns=["days", "negative", "neutral", "positive"])
                st.subheader('vader sentiment analysis')
                fig = px.bar(df, x="days", y=["negative", "neutral", "positive"], barmode='group', height=400)
                # fig.update_xaxes(ticktext=custom_labels, tickvals=df['weeks'])
                st.plotly_chart(fig)

            if data_size == "last week" and sentiment_model_selected == "vader":
                st.title("Sentiment analysis on last week dataset", anchor=None, help=None)
                df_list = []
                for day, day_analysis in tweets_week.iterrows():
                    current_day = []
                    current_day.append(str(day))
                    vader_negative = day_analysis['vader_SCORE_pnn_numeric'].count(-1.0)
                    current_day.append(vader_negative)

                    vader_neutral = day_analysis['vader_SCORE_pnn_numeric'].count(0.0)
                    current_day.append(vader_neutral)

                    vader_positive = day_analysis['vader_SCORE_pnn_numeric'].count(1.0)
                    current_day.append(vader_positive)
                    df_list.append(current_day)

                df = pd.DataFrame(df_list, columns=["days", "negative", "neutral", "positive"])
                st.subheader('vader sentiment analysis')
                fig = px.bar(df, x="days", y=["negative", "neutral", "positive"], barmode='group', height=400)
                # fig.update_xaxes(ticktext=custom_labels, tickvals=df['weeks'])
                st.plotly_chart(fig)

            if data_size == "last week" and sentiment_model_selected == "xlm_roBERTa":
                st.title("Sentiment analysis on last month dataset", anchor=None, help=None)
                df_list = []
                for day, day_analysis in tweets_week.iterrows():
                    current_day = []
                    current_day.append(str(day))
                    vader_negative = day_analysis['xlm_roberta_SCORE_numeric'].count(-1.0)
                    current_day.append(vader_negative)

                    vader_neutral = day_analysis['xlm_roberta_SCORE_numeric'].count(0.0)
                    current_day.append(vader_neutral)

                    vader_positive = day_analysis['xlm_roberta_SCORE_numeric'].count(1.0)
                    current_day.append(vader_positive)
                    df_list.append(current_day)

                df = pd.DataFrame(df_list, columns=["days", "negative", "neutral", "positive"])
                st.subheader('xlm sentiment analysis')
                fig = px.bar(df, x="days", y=["negative", "neutral", "positive"], barmode='group', height=400)
                # fig.update_xaxes(ticktext=custom_labels, tickvals=df['weeks'])
                st.plotly_chart(fig)

if __name__ == "__main__":
    st.set_page_config(page_icon="Logo_of_Twitter.png", page_title="SenForWirn2023")
    main()

