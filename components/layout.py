# components/layout.py
import streamlit as st

def create_responsive_layout(df):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<p class="selection-title">Select Statistics</p>', unsafe_allow_html=True)
        view = st.radio("Select Statistics", ["Daily", "Monthly", "Range"], horizontal=True, key="view_selector", label_visibility="collapsed")
    with col2:
        st.markdown('<p class="selection-title">Select portal</p>', unsafe_allow_html=True)
        portals = ['All'] + sorted(df['portal'].unique().tolist())
        selected_portal = st.selectbox("Select portal", portals, key="portal_selector", label_visibility="collapsed")
    return view, selected_portal

def create_footer():
    footer_html = """
    <div class="footer">
        <div class="footer-content">
            <div class="footer-column">
                <a href="/?page=home"target="_self">Home</a>
                <a href="/?page=about"target="_self">About Hindumisia.ai</a>
                <a href="/?page=benefits"target="_self">Benefits</a>
            </div>
            <div class="footer-column">
                <a href="/?page=anti_hindu_hate"target="_self">Anti-Hindu Hate</a>
                <a href="/?page=media_references"target="_self">Media References</a>
                <a href="/?page=partners"target="_self">Partners</a>
            </div>
            <div class="footer-column">
                <a href="/?page=privacy"target="_self">Privacy</a>
                <a href="/?page=ethics"target="_self">Ethics</a>
                <a href="/?page=contacts"target="_self">Contacts</a>
            </div>
            <div class="footer-column">
                <span>Connect with us</span>
                <div class="social-icons">
                    <a href="https://x.com/hindumisia"><img src="https://upload.wikimedia.org/wikipedia/commons/5/57/X_logo_2023_%28white%29.png" alt="X (Twitter)"></a>
                    <a href="https://www.instagram.com/hindumisia.ai/"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram"></a>
                </div>
                <div class="phone-social-icons">
                    <a href="https://x.com/hindumisia" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/5/57/X_logo_2023_%28white%29.png" alt="X (Twitter)"></a>
                    <a href="https://www.instagram.com/hindumisia.ai/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram"></a>
                </div>
            </div>
        </div>
        <div class="copyright">
            ⓒ 2024 hindumisia.ai All Rights Reserved
        </div>
    </div>
    """
    return footer_html