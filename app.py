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


df = pd.read_csv('기숙사수용현황eda.csv')
if univ != '' :
    df = df[df['학교'].str.count(univ) > 0]

col = ['지역', '학교', '설립구분', '재학생수(A)', '기숙사수용률', '입사경쟁률']

if add_radio == "1인실" :
    col = col + ['1인실실수','1인실식비','1인실기숙사비']
elif add_radio == "2인실" :
    col = col + ['2인실실수','2인실식비','2인실기숙사비']
elif add_radio == "3인실" :
    col = col + ['3인실실수','3인실식비','3인실기숙사비']
elif add_radio == "4인실" :
    col = col + ['4인실실수','4인실식비','4인실기숙사비']

df = df.loc[:, col]
st.dataframe(df)