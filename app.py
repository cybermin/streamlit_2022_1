import streamlit as st
import pandas as pd
import numpy as np

st.title('전국 대학 기숙사현황')

with st.sidebar:
    univ = st.text_input('대학명입력', '부산대학교')
    st.write('입력대학 : ', univ)

    add_radio = st.radio(
        "기숙사 유형선택",
        ("1인실", "2인실","3인실", '4인실')
    )
    st.write('유형 : ' , add_radio)