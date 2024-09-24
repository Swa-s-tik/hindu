# app.py
import streamlit as st
import streamlit.components.v1 as components
from components.layout import create_footer
from ml.data_processing import load_data
from pages import home, about
from PIL import Image
from utils import helpers

# Set page configuration
st.set_page_config(
    page_title="Hindumisia.ai",
    page_icon="🗞️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Google Tag Manager script
GTM_code = """
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NSM7Q9H8');</script>
<!-- End Google Tag Manager -->
"""

# Render the Google Tag Manager in the app
components.html(GTM_code, height=0)

helpers.load_html(r'styles\app_struct.html')

# Load the CSS file
helpers.load_css(r'styles\main.css')

# Load and display the logo
logo = Image.open(r"images\hindumisia-dark-bg-logo.jpg")


# Create the top banner with logo and title
st.markdown("""
    <div class="top-bar">
        <div class="dashboard-title">MEDIA SENTIMENT SCORECARD</div>
    </div>
    """, unsafe_allow_html=True)

# Display the logo image
st.image(logo, width=150, use_column_width=False)


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
    
    st.markdown(create_footer(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
