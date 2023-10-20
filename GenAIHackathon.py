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

# Add custom CSS to style the image buttons
st.markdown(
    """
    <style>
    .img-button {
        background-image: url('cv_image.png');
        background-size: cover;
        width: 200px;
        height: 200px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        border: none;
        padding: 0;
    }
    .img-button:hover {
        opacity: 0.7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a sidebar with image buttons for navigation
st.sidebar.title("Select a Page")

if st.button("", key="cv_button", on_click=build_cv_page, output_format="image"):
    pass

if st.button("", key="cover_letter_button", on_click=build_cover_letter_and_interview_page, output_format="image"):
    pass

if st.button("", key="career_options_button", on_click=explore_career_options_page, output_format="image"):
    pass
