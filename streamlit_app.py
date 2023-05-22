import streamlit as st
import pandas as pd
import altair as alt

# Example data
data = {
    'Element': ['A', 'B', 'C', 'D'],
    'Value1': [10, 15, 5, 12],
    'Value2': [8, 7, 6, 10],
    'Value3': [5, 9, 15, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Melt DataFrame to transform columns into rows
df_melted = df.melt('Element', var_name='Value', value_name='Count')

# Sort DataFrame by 'Element' and 'Value' columns
df_melted = df_melted.sort_values(['Element', 'Value'])

# Define the ordering of the 'Value' categories
value_order = ['Value1', 'Value2', 'Value3']

# Create bar chart using Altair
chart = alt.Chart(df_melted).mark_bar().encode(
    x=alt.X('Element', sort=None),
    y='Count',
    color=alt.Color('Value', sort=value_order),
    column=alt.Column('Value', sort=value_order),
).properties(
    width=20  # Adjust the width of each column
)

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)