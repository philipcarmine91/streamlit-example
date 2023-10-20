import streamlit as st

# Define the function for each page
def build_cv_page():
    st.title("Build your CV")
    # Add content for the "Build your CV" page here
    st.write("This is the content for 'Build your CV' page.")

def build_cover_letter_and_interview_page():
    st.title("Build a Cover Letter and Prepare for Interviews")
    # Add content for the "Build a Cover Letter and Prepare for Interviews" page here
    st.write("This is the content for 'Build a Cover Letter and Prepare for Interviews' page.")

def explore_career_options_page():
    st.title("Explore your Career Options")
    # Add content for the "Explore your Career Options" page here
    st.write("This is the content for 'Explore your Career Options' page.")

# Create a dictionary to map page names to functions
page_dict = {
    "Build your CV": build_cv_page,
    "Build a Cover Letter and Prepare for Interviews": build_cover_letter_and_interview_page,
    "Explore your Career Options": explore_career_options_page,
}

# Create a sidebar with images as buttons for navigation
st.sidebar.image("cv_image.png", use_column_width=True, output_format="PNG")
st.sidebar.image("cover_letter_image.png", use_column_width=True, output_format="PNG")
st.sidebar.image("career_options_image.png", use_column_width=True, output_format="PNG")

# Get the user's choice from the sidebar
selected_page = st.sidebar.selectbox("Select a Page", list(page_dict.keys()))

# Call the corresponding function based on the user's choice
page_dict[selected_page]()
