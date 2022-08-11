import streamlit as st
import pandas as pd
import numpy as np

st.title('전국 대학 기숙사현황')

with st.sidebar:
    add_radio = st.radio(
        "기숙사 융형선택",
        ("1인실", "2인실","3인실", '4인실')
    )
    st.write(add_radio)