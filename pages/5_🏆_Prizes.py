import streamlit as st

st.set_page_config(
    page_title="Prizes", page_icon="🏆"
)
st.sidebar.image('./imgs/lefttop_logo1.png', use_column_width=True)

st.write("### 🏆Prizes")

st.write("#### Prizes")

st.markdown("""
We have carefully designed award categories for each task to recognize outstanding contributions and to incentivize innovation, creativity, and excellence in the field of social media behavior analysis. 
The awards are as follows:
* Gold Prize: 1 per task. 
* Silver Prize: 1 per task.   
* Bronze Prize: 1 per task. 
* Top Student Group: 1 per task. The highest performing student team with members are students enrolled in a high school or university degree. 
""")


st.write("#### Scoring")

st.markdown("""
The evaluation of submissions for each award category is based on predefined criteria tailored to the objectives of the respective task. 
These criteria encompass factors including performance (60\%), scalability (20\%), and innovation (20\%). 
The approaches that made efficient use of large language models or graph foundation models are highly encouraged. 
A panel of expert judges, comprising domain specialists and data science professionals, rigorously assesses each submission against these criteria to ensure fairness and impartiality in the award selection process.
""")