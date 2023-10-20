import streamlit as st

# Define the function for each page
def build_cv_page():
    st.title("Build your CV")
    # Add content for the "Build your CV" page here

def build_cover_letter_and_interview_page():
    st.title("Build a Cover Letter and Prepare for Interviews")
    # Add content for the "Build a Cover Letter and Prepare for Interviews" page here

def explore_career_options_page():
    st.title("Explore your Career Options")
    # Add content for the "Explore your Career Options" page here

# Create a dictionary to map page names to functions
page_dict = {
    "Build your CV": build_cv_page,
    "Build a Cover Letter and Prepare for Interviews": build_cover_letter_and_interview_page,
    "Explore your Career Options": explore_career_options_page,
}

# Create a sidebar with image buttons for navigation using HTML
st.sidebar.title("Select a Page")

# Use HTML to create buttons with images
cv_image = open("cv_image.png", "rb").read()
if st.sidebar.button(f"<img src='data:image/png;base64,{cv_image}'/>", key="cv_button"):
    page_dict["Build your CV"]()

cover_letter_image = open("cover_letter_image.png", "rb").read()
if st.sidebar.button(f"<img src='data:image/png;base64,{cover_letter_image}'/>", key="cover_letter_button"):
    page_dict["Build a Cover Letter and Prepare for Interviews"]()

career_options_image = open("career_options_image.png", "rb").read()
if st.sidebar.button(f"<img src='data:image/png;base64,{career_options_image}'/>", key="career_options_button"):
    page_dict["Explore your Career Options"]()
