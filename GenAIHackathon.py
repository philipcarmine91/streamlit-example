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

# Create a title and center it
st.title("Welcome! Please choose from the options below:")
st.markdown("---")

# Use st.columns to center-align the images as buttons
col1, col2, col3 = st.columns(3)

# Add images as buttons for navigation
with col1:
    if st.image("cv_image.png"):
        page_dict["Build your CV"]()

with col2:
    if st.image("cover_letter_image.png"):
        page_dict["Build a Cover Letter and Prepare for Interviews"]()

with col3:
    if st.image("career_options_image.png"):
        page_dict["Explore your Career Options"]()
