import streamlit as st
import time
import io
import pandas as pd
import numpy as np

st.set_page_config(page_title="Task 2: Bursty Event Cascade Classification", page_icon="⚔️")
st.sidebar.image('./imgs/lefttop_logo1.png', use_column_width=True)

st.markdown("### ⚔️Task 2: Bursty Event Cascade Classification")
st.write(
    "#### Introduction"
)
st.write(
    """
The bursty event cascade classification task aims to classify social network structures as either the cascade of bursty events or normal events. 
Efficient classification of bursty event cascade enables the early detection of bursty events, safeguarding the integrity of online discourse and public perception.  """
)


st.write(
    "#### Dataset"
)
st.write(
"""
For the bursty event cascade classification challenge, we collect a dataset from Weibo comprising a total of 15,110 cascades. 
This dataset encompasses 6,346 cascades representing bursty events and 8,764 cascades representing normal events.
Specifically, the dataset is partitioned into 13,599 cascades for training and 1,511 cascades for testing. 
The dataset comprises posts made during the event, along with interactions such as shares, forming a cascade network.
The dataset is labeled with the event class for each cascade network.
Within the cascade network, each node represents a Weibo post, while edges symbolize share interactions between posts.
""")

st.success("**Dataset Download:** https://drive.google.com/drive/folders/1Pg9Hi6CM7xCsKqE341TfaQmoWmi31bqe?usp=sharing")
st.write(
"""
**Dataset Description:** The dataset comprises two files `train.json` and `test.json`. 
The `test.json` file does not contain labels.
Each instance in the dataset is represented as a dictionary, describing a cascade network. 
The dictionary includes the following fields, each with its corresponding meanings:
"""
)
dataset_description = [
    ['edge_index', ' This field represents the edges of the cascade network, denoting the Weibo share interactions. It is structured as a 2D array with a shape of `[2, edge_num]`, where `edge_num` signifies the number of interactions within the cascade.'],
    ['x', 'This field contains the feature embeddings of each Weibo post in the cascade network. These embeddings represent the content of the Weibo posts processed by BERT, a language model known for its contextual representation learning.'],
    ['label', 'This field indicates the label of the event class associated with the cascade network. It serves as the ground truth for classification tasks, distinguishing between bursty events and normal events.'],
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
    """The evaluation metric is the F1 score, the harmonic mean of the precision and recall."""
)


st.write(
    "#### Submission Rules"
)
st.write(
"""
There is no limit to the number of submissions per team. The final assessment will be based on the team's most recent submission, which will be publicly disclosed on the Leaderboard.
Each submission must be compressed into a `.zip` file uniquely identified by the team's ID (e.g., `Ix9oW1.zip`). 
The zip file should contain a single folder named `source_code` and two files named `result.json` and `introduction.pdf`.

* Result

The `result.json` file should consist of a list of predictions, aligned with the order of data in `test.json`. 
The example format of the `result.json` file is as follows:
```
[0, 1, 0, 1, 0, ..., 1, 0, 0]
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
