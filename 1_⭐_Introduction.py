import select
import markdown_it
import streamlit as st
import base64
from PIL import Image

st.set_page_config(
    page_title="Characterizing User Behavior in Social Networks: Propagation, Prediction, and Sensemaking", page_icon="⭐"
)

st.sidebar.image('./imgs/lefttop_logo1.png', use_column_width=True)

# st.markdown("""
# <style>
#     [data-testid=stSidebar] {
#         background-color: #1e1c63;
#         color: #FFFFFF;
#     }
# </style>
# """, unsafe_allow_html=True)

# =============================
# set background
# def set_bg_hack_url(side_bg):
#     '''
#     A function to unpack an image from url and set as bg.
#     Returns
#     -------
#     The background.
#     '''
#     side_bg_ext = 'png'
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#             background: rgba(0, 0, 0, {0.2});
#             background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
#             background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )
# set_bg_hack_url("./imgs/top.jpg")

# set top title
st.markdown("""
    <div style="text-align:center;">
        <p style="font-size: 34px; color: rgb(30, 28, 99); margin-bottom: 5px;"><b>IEEE Big Data 2024</b></p>
        <p style="font-size: 28px; color: rgb(30, 28, 99); margin-bottom: 10px;">Washington DC, USA</p>
    </div>
""", unsafe_allow_html=True)

# ============================
# begin
st.write("### ⭐Characterizing User Behavior in Social Networks: Propagation, Prediction, and Sensemaking")


st.image('./imgs/background.jpg', use_column_width=True)

# st.sidebar.success("在上方选择一个演示。")

st.markdown(
"""
Social media platforms have been serving as crucial hubs for online communication, information dissemination, and social interaction. 
Social network services have become important and efficient platforms for users to share all kinds of information. 
The capability to monitor user-generated content and users' behavior from information diffusion in those social networks facilitates a wide range of real-life applications, including but not limited to marketing, public health, and sociology. 
The proposed challenge traverses multiple disciplines, including sociology, cybersecurity, and psychology, fostering interdisciplinary collaboration and knowledge exchange. 

#### Challenges
This challenge aims to foster advancements in characterizing user behavior in social networks by addressing three pivotal tasks:
"""
)
page_path = "./pages/2_⚔️_Task_1.py"
st.markdown(
"""
* *[Retweet network link prediction](Task_1)*: This task is centered around predicting the likelihood of retweet behavior between users in a social network. By accurately forecasting retweet connections, we aim to gain insights into information diffusion dynamics and user engagement patterns on social media platforms.
* *[Bursty event cascade classification](Task_2)*: In this task, the objective is to classify social network structures as either cascades of bursty events or normal events. By discerning between these two types of events, we seek to uncover patterns associated with sudden surges in activity and distinguish them from typical social network behaviors.
* *[Multi-modal social media content intention recognition](Task_3)*: This task focuses on inferring the underlying intent behind multi-modal social media content. By generating insights into user intentions, we can enhance our understanding of user behavior and communication patterns on social media platforms.

The challenge starts from predicting user online behavior through the analysis of their interactions and relationships on social platforms, while also enhancing comprehension of their behavior pattern (bursty cascade classification task) and posting intentions (intention recognition task). 
This process necessitates not only an understanding of visual and linguistic information but also complex multi-modal reasoning capabilities. The three sub-tasks are interrelated and collaboratively contribute to a cohesive, human-centric perception and cognition solution for social network behavior. 
""", unsafe_allow_html=True)


pages = {
    "Introduction": "introduction",
    "Task 1": "2_⚔️_Task_1",
    "Task 2": "task2"
}
# if st.markdown("Go to Timeline"):
#     st.switch_page("pages/1_📅_Timeline.py")