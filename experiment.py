# import inspect
# import textwrap
#
# import streamlit as st
#
# from demo_echarts import ST_DEMOS
# from demo_pyecharts import ST_PY_DEMOS
#
#
# def main():
#     st.title("Streamlit ECharts Demo")
#
#     with st.sidebar:
#         st.header("Configuration")
#         api_options = ("echarts", "pyecharts")
#         selected_api = st.selectbox(
#             label="Choose your preferred API:",
#             options=api_options,
#         )
#
#         page_options = (
#             list(ST_PY_DEMOS.keys())
#             if selected_api == "pyecharts"
#             else list(ST_DEMOS.keys())
#         )
#         selected_page = st.selectbox(
#             label="Choose an example",
#             options=page_options,
#         )
#         demo, url = (
#             ST_DEMOS[selected_page]
#             if selected_api == "echarts"
#             else ST_PY_DEMOS[selected_page]
#         )
#
#         if selected_api == "echarts":
#             st.caption(
#                 """ECharts demos are extracted from https://echarts.apache.org/examples/en/index.html,
#             by copying/formattting the 'option' json object into st_echarts.
#             Definitely check the echarts example page, convert the JSON specs to Python Dicts and you should get a nice viz."""
#             )
#         if selected_api == "pyecharts":
#             st.caption(
#                 """Pyecharts demos are extracted from https://github.com/pyecharts/pyecharts-gallery,
#             by copying the pyecharts object into st_pyecharts.
#             Pyecharts is still using ECharts 4 underneath, which is why the theming between st_echarts and st_pyecharts is different."""
#             )
#
#     demo()
#
#     sourcelines, _ = inspect.getsourcelines(demo)
#     with st.expander("Source Code"):
#         st.code(textwrap.dedent("".join(sourcelines[1:])))
#     st.markdown(f"Credit: {url}")
#
#
# if __name__ == "__main__":
#     st.set_page_config(
#         page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
#     )
#     main()
#     with st.sidebar:
#         st.markdown("---")
#         st.markdown(
#             '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
#             unsafe_allow_html=True,
#         )
#         st.markdown(
#             '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
#             unsafe_allow_html=True,
#         )

"""
import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime, timedelta


st.set_page_config(layout="centered", page_icon="Logo_of_Twitter.png",page_title="SenForWirn2023")
st.title("Sentiment analysis by week", anchor=None, help=None)

data = pd.read_csv('data/all_at_21_05_2023.csv', index_col=[0])
data['created_at'] = pd.to_datetime(data['created_at'])
data.set_index("created_at", inplace=True)
# print(data)
tweets_by_week = data.resample('W').apply(list)

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

# display del dataset
st.dataframe(df)


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

# display del dataset
st.dataframe(df)
"""