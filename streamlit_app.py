import inspect
import textwrap
import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime, timedelta

import streamlit as st




def main():
    st.title("Sentiment analysis by week", anchor=None, help=None)

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
            st.caption(
                """A lato viene mostrata le sentiment analysis prodotte da i modelli "vader" e "xlm roBERTa" """
            )
        if analysis_type_selected == "topic analysis":
            st.caption(
                """A lato viene mostrata la topic analysis prodotta da "Bertopic model" """
            )

    # demo()

    # sourcelines, _ = inspect.getsourcelines(demo)
    # with st.expander("Source Code"):
        # st.code(textwrap.dedent("".join(sourcelines[1:])))
    # st.markdown(f"Credit: {url}")


if __name__ == "__main__":
    st.set_page_config(page_icon="Logo_of_Twitter.png", page_title="SenForWirn2023")
    main()

