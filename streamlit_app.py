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
        api_options = ("sentiment analysis", "topic analysis")
        selected_api = st.selectbox(
            label="Seleziona il tipo di analisi",
            options=api_options,
        )

        page_options = (
            # list(ST_PY_DEMOS.keys())
            # if selected_api == "pyecharts"
            # else list(ST_DEMOS.keys())
        )
        selected_page = st.selectbox(
            label="Choose an example",
            options=page_options,
        )
        # demo, url = (
            # ST_DEMOS[selected_page]
            # if selected_api == "echarts"
            # else ST_PY_DEMOS[selected_page]
        # )

        if selected_api == "echarts":
            st.caption(
                """ECharts demos are extracted from https://echarts.apache.org/examples/en/index.html, 
            by copying/formattting the 'option' json object into st_echarts.
            Definitely check the echarts example page, convert the JSON specs to Python Dicts and you should get a nice viz."""
            )
        if selected_api == "pyecharts":
            st.caption(
                """Pyecharts demos are extracted from https://github.com/pyecharts/pyecharts-gallery,
            by copying the pyecharts object into st_pyecharts. 
            Pyecharts is still using ECharts 4 underneath, which is why the theming between st_echarts and st_pyecharts is different."""
            )

    # demo()

    # sourcelines, _ = inspect.getsourcelines(demo)
    # with st.expander("Source Code"):
        # st.code(textwrap.dedent("".join(sourcelines[1:])))
    # st.markdown(f"Credit: {url}")


if __name__ == "__main__":
    st.set_page_config(page_icon="Logo_of_Twitter.png", page_title="SenForWirn2023")
    main()

