import streamlit as st
import time
import io
import numpy as np

st.set_page_config(page_title="Task 3: Multimodal Intention Recognition for Social Media", page_icon="⚔️")

st.markdown("## ⚔️Task 3: Multimodal Intention Recognition for Social Media")
st.write(
    "### Introduction"
)
st.write(
"""
The multimodal intention recognition task aims to recognize the underlying intent (e.g., informational, emotional, promotional) behind multi-modal social media content (e.g., text-image pairs). 
Recognizing the intention behind multimodal social media content facilitates a deeper understanding of user behavior and preferences, and accurately grasp the motives behind user posts, thereby deepening our understanding of user behavior.  
"""
)


st.write(
    "### Dataset"
)
st.write(
"""
For the challenge, we collected a mutlimodal social intention dataset containing 979 twitter anotated with 7868 intentions. 
The intentions include nine different types of intentions extracted from ATOMIC and one open-domain intention. 
Specifically, nine ATOMIC-extracted intentions include ''xNeed'' (user's need), ''xIntent'' (user's intention), ''xAttr'' (user's attribute), 
''xEffect'' (effect of user's action), ''xReact'' (user's reaction), ''xWant'' (user's desire), ''oEffect'' (impact on others), 
''oReact'' (others' reaction), and ''oWant'' (others' desire), where ''x'' represents the thoughts and behaviors of the user after posting, 
and ''o'' denotes the impact of the post on others. 
The open intention, termed ''Open'', describes the motive and purpose behind a user's decision to publish a specific post content. 
Each intention is annotated with Label Studio where five annotators evaluate generated candidates' intentions alongside raw text-image pairs. 
""")


st.success("**Dataset Download:** https://juejin.cn/post/7268955025211342859#heading-8")
st.write(
"""
**Dataset Description:** The dataset comprises two files and a floder:  `train.json`, `test.json` and `image`. 

Each instance in the `train.txt` and `test.json` is represented as a dictionary, describing a tweet.
The dictionary includes the following fields, each with its corresponding meanings:
"""
)
dataset_description = [
    ['intention_labels', ' This field represents the edges of the cascade network, denoting the Weibo share interactions. It is structured as a 2D array with a shape of `[2, edge_num]`, where `edge_num` signifies the number of interactions within the cascade.'],
    ['x', 'The tweet image file, according to this name, you can find the image the `image` floder'],
    ['text', 'This field indicates the label of the event class associated with the cascade network. It serves as the ground truth for classification tasks, distinguishing between bursty events and normal events.']
]



st.write(
    "### Metric"
)
st.write(
"""The evaluation metric is the average BERT score(reported as percentages) for the 10 different aspects of the generated intentions."""
)


st.write(
    "### Submission"
)
st.write(
"""
There is no limit to the number of submissions per team. The final assessment will be based on the team's most recent submission, which will be publicly disclosed on the Leaderboard.

Each submission must be compressed into a `.zip` file uniquely identified by the team's ID (e.g., `Ix9oW1.zip`). The zip file should contain a single folder named `source_code` and one file named `result.json`.

The `source_code` folder should encompass all necessary source code and saved models. It must include an executable `evaluation.py` file capable of testing the provided data in `test.json` and generating the corresponding `result.json` file.

The `result.json` file should consist of a list of predictions, aligned with the order of data in `test.json`, formatted as `[0, 1, 0, 1, 0, ..., 1, 0, 0]`.

The specified directory structure for the submitted file is as follows:
```
{team_id}.zip
    - source_code
        - evaluation.py
        - ...
    - result.json
```
"""
)

st.markdown("---")
st.warning("Only submissions that fully comply with the provided submission rules will be accepted for evaluation.")
uploaded_file = st.file_uploader("Submit a `.zip` file named only after the team ID.")
submit_button = st.button("Submit")
if submit_button:
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Display a message indicating file upload in progress
        st.info(f"You selected '{uploaded_file.name}'. File upload in progress. Please wait...")

        # Process the uploaded file
        file_contents = uploaded_file.getvalue()
        file_obj = io.BytesIO(file_contents)
        with open(uploaded_file.name, "wb") as f:
            f.write(file_contents)
        file_path = f.name

        # Display a success message indicating file upload is complete
        st.success("File upload complete!")
    else:
        st.error("Please upload a file before submitting.")
