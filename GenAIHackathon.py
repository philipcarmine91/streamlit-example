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

# Create a sidebar with image buttons for navigation
st.sidebar.title("Select a Page")

# Use st.button with an image to show images as buttons
if st.sidebar.button("", key="cv_button", on_click=build_cv_page):
    st.image("cv_image.png", use_column_width=True, output_format="PNG")

if st.sidebar.button("", key="cover_letter_button", on_click=build_cover_letter_and_interview_page):
    st.image("cover_letter_image.png", use_column_width=True, output_format="PNG")

if st.sidebar.button("", key="career_options_button", on_click=explore_career_options_page):
    st.image("career_options_image.png", use_column_width=True, output_format="PNG")
