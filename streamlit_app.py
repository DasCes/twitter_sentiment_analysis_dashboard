import streamlit as st
import pandas as pd

# Example data
data = {
    'Element': ['A', 'B', 'C', 'D'],
    'Category1': [10, 15, 5, 12],
    'Category2': [8, 7, 6, 10],
    'Category3': [5, 9, 15, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set 'Element' column as index
df.set_index('Element', inplace=True)

# Display bar chart
st.bar_chart(df)