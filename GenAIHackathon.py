import streamlit as st

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

# Create a sidebar with image buttons for navigation
with st.sidebar:
    st.header("Navigation")
    cv_button = st.button("Build your CV", key="cv_button")
    cover_letter_button = st.button("Build a Cover Letter and Prepare for Interviews", key="cover_letter_button")
    career_options_button = st.button("Explore your Career Options", key="career_options_button")

# Get the user's choice based on which button they click
if cv_button:
    page_dict["Build your CV"]()
elif cover_letter_button:
    page_dict["Build a Cover Letter and Prepare for Interviews"]()
elif career_options_button:
    page_dict["Explore your Career Options"]()
