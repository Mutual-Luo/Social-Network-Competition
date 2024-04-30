import streamlit as st
# import csv
# import secrets
# import string
# import io

# def generate_team_id(length=6):
#     alphabet = string.ascii_uppercase + string.digits
#     return ''.join(secrets.choice(alphabet) for _ in range(length))

st.set_page_config(page_title="Registration", page_icon="📋")
st.sidebar.image('./imgs/lefttop_logo1.png', use_column_width=True)
st.markdown("### 📋Registration")


st.markdown(
"""
Register your team to participate in the *Characterizing User Behavior in Social Networks: Propagation, Prediction, and Sensemaking 2024*. 
Each team consists of at least one captain and up to five other members. 
"""
)

st.success("Please complete the registration form: [Link](https://docs.google.com/forms/d/e/1FAIpQLScfrY1fvHLOswdSFS66bvO7dasbayiGSlTRE2fxTDZvJ6W_sA/viewform?usp=sf_link)")


# def write_to_csv(data):
#     with open('./table/registration.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(data)


# with st.form(key='my_form'):
#     team_name = st.text_input("Team's name (required):", key='1')
#     leader_name = st.text_input("Leader's name (required):", key='2')
#     leader_email = st.text_input("Leader's email address (required):", key='3')
#     leader_affiliation = st.text_input("Leader's affiliation (required):", key='4')
#     other_members_names = st.text_input("Other team members' name. Please list members separated by commas.")
#     other_members_emails = st.text_input("Other team members' email address. Please list members separated by commas.")
#     other_members_affiliations = st.text_input("Other team members' affiliation. Please list members separated by commas.")
#     st.markdown("Note that the information of other team members should correspond one-to-one.")
    
#     # Form submission button
#     if st.form_submit_button(label='提交'):
#         # Check if required fields are empty
#         if not (team_name and leader_name and leader_email and leader_affiliation):
#             st.error('Error: Team name, leader name, leader email, and leader affiliation are required.')
#         else:
#             # Generate a unique team ID
#             team_id = generate_team_id()
#             # Write form data and team ID to CSV file
#             team_members = other_members_names.split(',')
#             member_emails = other_members_emails.split(',')
#             member_affiliations = other_members_affiliations.split(',')
            
#             # Ensure the number of names, emails, and affiliations match
#             if len(team_members) == len(member_emails) == len(member_affiliations):
#                 for i in range(len(team_members)):
#                     write_to_csv([team_id, team_name, leader_name, leader_email, leader_affiliation, team_members[i], member_emails[i], member_affiliations[i]])
#                 st.success(f'Form data submitted successfully! Your team ID is: {team_id}')
#                 st.warning("Make sure to note down your team ID. You'll need it when submitting your resolutions.")
#             else:
#                 st.error('Error: Number of team members, emails, and affiliations should match.')
