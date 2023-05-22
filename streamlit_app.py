import streamlit as st
import pandas as pd
import altair as alt

# Example data
data = {
    'Element': ['A', 'B', 'C', 'D'],
    'Category1': [10, 15, 5, 12],
    'Category2': [8, 7, 6, 10],
    'Category3': [5, 9, 15, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Melt DataFrame to transform columns into rows
df_melted = df.melt('Element', var_name='Category', value_name='Value')

# Create bar chart using Altair
chart = alt.Chart(df_melted).mark_bar().encode(
    x='Element',
    y='Value',
    color='Category',
    column='Category'
).properties(
    width=100  # Adjust the width of each column
)

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)