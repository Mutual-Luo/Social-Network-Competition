import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Leaderboard", page_icon="📈")

st.markdown("## 📈Leaderboard")

st.warning("Updated weekly before Monday, Beijing time.")

st.markdown("#### Task 1: Retweet Network Link Prediction(Stage 1)")
leaderbord1 =  pd.read_csv("./table/leaderbord1.csv")
st.write(leaderbord1)

st.markdown("#### Task 2: Bursty Event Cascade Classification(Stage 1)")
leaderbord2 =  pd.read_csv("./table/leaderbord2.csv")
st.write(leaderbord2)

st.markdown("#### Task 3: Multimodal Intention Recognition for Social-Media(Stage 1)")
leaderbord2 =  pd.read_csv("./table/leaderbord2.csv")
st.write(leaderbord2)