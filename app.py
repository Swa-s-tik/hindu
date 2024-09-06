# app.py
import streamlit as st
from components import layout
from ml.data_processing import load_data
from pages import home, about

# Set page configuration
st.set_page_config(
    page_title="Hindumisia.ai",
    page_icon="🗞️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load and display the logo
#logo = Image.open(r"C:\Users\Swastik\Desktop\hindu\hindumisia-dark-bg-logo.png")

# Create the top banner with logo and title
st.markdown("""
    <div class="top-bar">
        <div class="dashboard-title">MEDIA SENTIMENT SCORECARD</div>
    </div>
    """, unsafe_allow_html=True)

# Display the logo image
st.image(r"C:\Users\Swastik\Desktop\hindu\hindumisia-dark-bg-logo.png", width=150, use_column_width=False)

# Add custom CSS to position the logo
st.markdown("""
    <style>
    img {
        position: relative;
        z-index: 1100;
        left: 0px
        top: 0px;
        transform: translate(-25px, -135px);
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Get the current page from the URL parameter
    page = st.query_params.get("page", "home")

    if page == "home":
        # Load data
        df = load_data()

        # Radio buttons for selecting the view
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<p class="selection-title">Select Statistics</p>', unsafe_allow_html=True)
            view = st.radio("Select Statistics", ["Daily", "Monthly", "Range"], horizontal=True, key="view_selector", label_visibility="collapsed")

        if view == "Daily":
            home.main_dashboard(df)
        elif view == "Monthly":
            home.monthly_dashboard(df)
        else:
            home.range_dashboard(df)
    else:
        # Import and run the appropriate page module
        module = __import__(f"pages.{page}", fromlist=["run_page"])
        module.run_page()
    
    layout.create_footer()

if __name__ == "__main__":
    main()
