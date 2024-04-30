import streamlit as st
import time
import io
import numpy as np
import pandas as pd

st.set_page_config(page_title="Task 3: Multimodal Intention Recognition for Social Media", page_icon="⚔️")
st.sidebar.image('./imgs/lefttop_logo1.png', use_column_width=True)

st.markdown("### ⚔️Task 3: Multimodal Intention Recognition for Social Media")
st.write(
    "#### Introduction"
)
st.write(
"""
The competition focuses on a challenging text generation task: multimodal intention recognition. 
The multimodal intention recognition task aims to recognize the underlying intent (e.g., informational, emotional, promotional) behind multi-modal social media content (e.g., text-image pairs). 
Recognizing the intention behind multimodal social media content facilitates a deeper understanding of user behavior and preferences, and accurately grasp the motives behind user posts, thereby deepening our understanding of user behavior.  
"""
)


st.write(
    "#### Dataset"
)
st.write(
"""
For the challenge, we collected a mutlimodal social intention dataset containing 979 Twitter posts anotated with 7868 intentions. 
Specifically, the dataset is partitioned into 881 Twitter posts for training and 98 Twitter posts for testing. 
The intentions include nine different types of intentions extracted from ATOMIC and one open-domain intention. 
Specifically, nine ATOMIC-extracted intentions include ''xNeed'' (user's need), ''xIntent'' (user's intention), ''xAttr'' (user's attribute), 
''xEffect'' (effect of user's action), ''xReact'' (user's reaction), ''xWant'' (user's desire), ''oEffect'' (impact on others), 
''oReact'' (others' reaction), and ''oWant'' (others' desire), where ''x'' represents the thoughts and behaviors of the user after posting, 
and ''o'' denotes the impact of the post on others. 
The open intention, termed ''Open'', describes the motive and purpose behind a user's decision to publish a specific post content. 
Each intention is annotated with Label Studio where five annotators evaluate generated candidates' intentions alongside raw text-image pairs. 
""")


st.success("**Dataset Download:** [Link](https://drive.google.com/drive/folders/1I9qtG74-9dxNS8iKxHzDPe8hb_wSK38u?usp=sharing)")
st.write(
"""
**Dataset Description:** The dataset comprises two files and a floder:  `train.json`, `test.json` and `image`. 
The `test.json` file does not contain `intentions`. Participants are required to generate intentions for the test instances based on the provided text and image data.

Each instance in the `train.txt` and `test.json` is represented as a dictionary, delineating the attributes of an individual tweet..
The dictionary includes the following fields, each with its corresponding meanings:
"""
)
dataset_description = [
    ['intention_labels', 'This field contains a list of labels. if `intention_labels[3]` equals 1, it signifies that `Intention 3` is the ground truth for the intention of this tweet.'],
    ['image', 'This field denotes the file of the tweet image. Correspondingly, the image file can be located in the `image` folder based on this provided name.'],
    ['text', ' This field encompasses the textual content of the tweet.'],
    ['intentions', 'A dictionary comprising entries from `Intention 1` to `Intention 10`'],
]
columns = ['Field', 'Meaning']
dataset_description = pd.DataFrame(dataset_description, columns=columns)
# st.table(dataset_description)
st.markdown(dataset_description.style.hide(axis="index").to_html(), unsafe_allow_html=True)
st.markdown("""
""")


st.write(
    "#### Metric"
)
st.write(
"""The evaluation metric is the average BERT score(reported as percentages) for the 10 different aspects of the generated intentions."""
)


st.write(
    "#### Submission"
)
st.write(
"""
There is no limit to the number of submissions per team. The final assessment will be based on the team's most recent submission, which will be publicly disclosed on the Leaderboard.
Each submission must be compressed into a `.zip` file identified by the team's name (e.g., `Ix9oW1.zip`). 
The zip file should contain a single folder named `source_code` and two files named `result.json` and `introduction.pdf`.

* Result

The `result.json` file should be structed as a list of dictionaries, aligned with the order of data in `test.json`. 
Each dictionary corresponds to a tweet and contains all generative intentions for that tweet. 
In cases where the value at position `i` in the `intention_labels` list is `0`, the corresponding `Intention i`  is represented as an empty string. 
The example format of the `result.json` file is as follows:
```
[
    {
        "Intention 1": "", 
        "Intention 2": "This is Intention 2", 
        ...
    },
    {   
        "Intention 1": "hello1", 
        "Intention 2": "This is not Intention 2", 
        ...
    },
    ...
]
```

* Source Code

The `source_code` folder should encompass all necessary source code and saved models. It must include an executable `evaluation.py` file capable of testing the provided data in `test.json` and generating the corresponding `result.json` file.
During evaluation, the provided `test.json` file will be placed within the `source_code` directory alongside the `evaluation.py` file.
Therefore, participants need not include any additional data files in their submissions.

* Model Introduction

In the `introduction.pdf` file, participants are expected to present a detailed overview of their method. 
This introduction should offer insights into the innovative aspects of their approach, enabling better evaluation by the judges.
The innovation of the method will contribute to 20\% of the total score.

* The specified directory structure for the submitted file is as follows:
```
{team_id}.zip
    - source_code
        - evaluation.py
        - ...
    - result.json
    - introduction.pdf
```
"""
)
st.markdown("---")
st.write(
    "#### Submission Method"
)
st.warning("Only submissions that fully comply with the provided submission rules will be accepted for evaluation.")
st.markdown(
"""
Please upload your submission files to a secure and accessible platform, such as Google Drive or another suitable file hosting service. 
Once your files are uploaded, generate a shareable link. Ensure that this link allows download access. 
In the submission form provided, enter the generated download link for your files. 
""")
st.success("Submission Form: [Link](https://docs.google.com/forms/d/e/1FAIpQLSd0f76YEuJXf2mswHudrc5wpVgzZonbPEAHfiJBqLagdelQEg/viewform?usp=sf_link)")
# st.markdown("---")
# st.warning("Only submissions that fully comply with the provided submission rules will be accepted for evaluation.")
# uploaded_file = st.file_uploader("Submit a `.zip` file named only after the team ID.")
# submit_button = st.button("Submit")
# if submit_button:
#     # Check if a file has been uploaded
#     if uploaded_file is not None:
#         # Display a message indicating file upload in progress
#         st.info(f"You selected '{uploaded_file.name}'. File upload in progress. Please wait...")

#         # Process the uploaded file
#         file_contents = uploaded_file.getvalue()
#         file_obj = io.BytesIO(file_contents)
#         with open(uploaded_file.name, "wb") as f:
#             f.write(file_contents)
#         file_path = f.name

#         # Display a success message indicating file upload is complete
#         st.success("File upload complete!")
#     else:
#         st.error("Please upload a file before submitting.")
