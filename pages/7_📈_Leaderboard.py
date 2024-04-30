import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Leaderboard", page_icon="📈")
st.sidebar.image('./imgs/lefttop_logo1.png', use_column_width=True)

st.markdown("### 📈Leaderboard")

st.warning("The leaderboard will be refreshed weekly, with updates scheduled in Monday, Beijing Time (BJT). The next update is planned for May 6, 2024.")

st.markdown("#### Task 1: Retweet Network Link Prediction")
leaderbord1 =  pd.read_csv("./table/leaderbord1.csv")
# st.markdown(leaderbord1.style.hide(axis="index").to_html(), unsafe_allow_html=True)
st.write(leaderbord1)

st.markdown("#### Task 2: Bursty Event Cascade Classification")
leaderbord2 =  pd.read_csv("./table/leaderbord2.csv")
# st.markdown(leaderbord2.style.hide(axis="index").to_html(), unsafe_allow_html=True)
st.write(leaderbord2)

st.markdown("#### Task 3: Multimodal Intention Recognition for Social-Media")
leaderbord3 =  pd.read_csv("./table/leaderbord3.csv")
# st.markdown(leaderbord2.style.hide(axis="index").to_html(), unsafe_allow_html=True)
st.write(leaderbord3)