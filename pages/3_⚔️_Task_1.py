import streamlit as st
import time
import io
import numpy as np

st.set_page_config(page_title="Task 1: Retweet Network Link Prediction", page_icon="⚔️")
st.sidebar.image('./imgs/lefttop_logo1.png', use_column_width=True)

st.markdown("### ⚔️Task 1: Retweet Network Link Prediction")
st.write(
    "#### Introduction"
)
st.write(
    """The retweet network link prediction task aims to predict the retweet behavior between users in the social network. 
By predicting the retweet behavior patterns, insights can be gained into the mechanisms driving information diffusion, aiding in targeted content dissemination and audience engagement strategies. """
)


st.write(
    "#### Dataset"
)
st.write(
"""
For the challenge, we collect a retweet dataset from Weibo, which contains the retweet network of 1,563,421 users. 
In the retweet network, each node represents a user, and edges represent retweet relationships between users. ~
The weight of an edge signifies the number of times one user has retweeted content from another user. 
""")


st.success("**Dataset Download:** [Link](https://drive.google.com/drive/folders/1WdJqk8qsD7oVfk-JQ7Xc6fl3rRXCndkI?usp=drive_link)")
st.write(
"""
**Dataset Description:** The dataset comprises two files:  `train.txt` and `test.txt`. 

The `train.txt` file follows this format:
```
1563421
701683 871966 1
546410 304924 3
93571 927327 1
1307394 1150598 4
...
```
The first line indicates the total number of nodes in the dataset. 
From the second line onward, each line represents an edge in the network.
Each edge is characterized by three values: the source node ID, the target node ID, and the edge weight.
The source node ID and the target node ID identify the nodes linked by the edge, delineating retweet relations of two users in Weibo.
The edge weight denotes the number of retweets associated with the users involved in the interaction.

The `test.txt` file follows this format:
```
612169 229397
1210014 943698
1542231 53444
530523 207660
1084259 1263491
...
```
Each line represents a pair of users for which a retweet relationship needs to be predicted.
The line contains two values: the source node ID and the target node ID, representing the users involved in the potential retweet relationship.
If the predicted output is `1`, it indicates the presence of a retweet relationship between the two users.
Conversely, if the predicted output is `0`, it signifies the absence of a retweet relationship between the two users.
Notably, all the relationships listed in `test.txt` have been removed from the training data `train.txt`, ensuring that predictions are made for unseen relationships.
"""
)

st.write(
    "#### Metric"
)
st.write(
    """The evaluation metric is the F1 score, the harmonic mean of the precision and recall. """
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
st.write(
    "#### Submission Method"
)
st.warning("Only submissions that fully comply with the provided submission rules will be accepted for evaluation.")
st.markdown(
"""
Upload your submission files to a secure and accessible platform such as Google Drive or another suitable file hosting service. 
Once your files are uploaded, generate shareable link. Ensure that these links are set to allow download access. 
In the submission form provided, enter the generated download links for your files. 
""")
st.success("Submission Form: [Link](https://docs.google.com/forms/d/16xAcjOdf6BNz8V0hH-M59mNMq5_tF0rXDXBHW7a8bGM/edit)")
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

