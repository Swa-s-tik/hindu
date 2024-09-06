import streamlit as st

def run_page():
    st.title("Ethics")

    st.markdown("""
    We have been influenced by the writings of Professor Virginia Dignum of Umea University in Sweden and Professor Michael Wooldridge, University of Oxford in England to explain our commitment to ethical AI.
    """)

    st.markdown("""
    <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
    <strong>Disclaimer:</strong><br>
    We do not have any relationship (professional or personal) with the Professors or their Universities, nor have they been involved in the development of this tool in any capacity or whatsoever.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 10px 0; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
            <h2>Accountability</h2>
            <p><strong>Media Sentiment Scorecard ®</strong> uses information collected to prepare metrics and reports to track trends and gain insights about the nature of anti-Hindu hate prevalent in media platforms.</p>
            <p>We store all details that we source from media portals that are deemed relevant for further analysis and action. They are all publicly available information. Please refer to our <a href="/?page=privacy"target="_self">privacy policy</a> for additional information.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 10px 0; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
            <h2>Responsibility</h2>
            <p><strong>hindumisia.<span style='color: #FF9934;'>ai</strong> automates the process of identifying and flagging anti-Hindu articles based on an AI model developed by its founder. The founder has defined a proprietary anti-Hindu AI-based model to detect and flag articles as anti-Hindu.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 20px 0; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
        <h2>Transparency</h2>
        <div style="display: flex; gap: 20px;">
            <div style="flex: 1;">
                <h3>AI based NLP Model</h3>
                <p>The model does not use any personally identifiable information or any form of demographic information (gender, religion, location etc) to determine anti-Hindu hate. Only the article title text, which is publicly available, is used to determine anti-Hindu hate.</p>
            </div>
            <div style="flex: 1;">
                <h3>Data</h3>
                <p><strong>hindumisia.<span style='color: #FF9934;'>ai</span></strong> uses publicly available information to determine anti-Hindu hate. Please refer to our <a href="/?page=privacy" target="_self">privacy policy</a> for additional information.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_page()