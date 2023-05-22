import streamlit as st
import pandas as pd
import plotly.express as px

# continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
df = pd.DataFrame(
    [["Product A", 5.6, 7.8, 5], ["Product B", 5.8, 7.2, 4.9]],
    columns=["Product", "Comfort", "Sound", "Calls"]
)

fig = px.bar(df, x="weeks", y=["negative", "neutral", "positive"], barmode='group', height=400)
# st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig)