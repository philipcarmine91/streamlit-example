import streamlit as st

"""
# Hello!

Please choose from the following three options:

"""

# Define the function for each page
def build_cv_page():
    st.header("Build your CV")
    # Add content for the "Build your CV" page here

def build_cover_letter_and_interview_page():
    st.header("Build a Cover Letter and Prepare for Interviews")
    # Add content for the "Build a Cover Letter and Prepare for Interviews" page here

def explore_career_options_page():
    st.header("Explore your Career Options")
    # Add content for the "Explore your Career Options" page here

# Create a dictionary to map page names to functions
page_dict = {
    "Build your CV": build_cv_page,
    "Build a Cover Letter and Prepare for Interviews": build_cover_letter_and_interview_page,
    "Explore your Career Options": explore_career_options_page,
}

# Create a sidebar with buttons using images for navigation
st.sidebar.image("cv_image.png", use_column_width=True)
st.sidebar.image("cover_letter_image.png", use_column_width=True)
st.sidebar.image("career_options_image.png", use_column_width=True)

# Get the user's choice from the sidebar
selected_page = st.sidebar.selectbox("Select a Page", list(page_dict.keys()))

# Call the corresponding function based on the user's choice
page_dict[selected_page]()
