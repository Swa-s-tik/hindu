import streamlit as st

def run_page():
    st.markdown("# Privacy", unsafe_allow_html=True)
    
    questions = [
        ("Policy Brief", """
        <strong>hindumisia.<span style='color: #FF9934;'>ai</span></strong> collects only publicly available information from portals for use.

        There's no user registration requirements for using the website. So no personal information is collected in that regard. Please read on to know more about how we store and use the information we collect.
        """),
        ("Cookies", """
        We do not track website user behavior when they browse the website. So we don't use cookies. As simple as that.

        This privacy policy is subject to modifications from time to time in alignment with our evolving needs. We will update this section as and when our privacy policy changes.
        """),
        ("Information we collect and use", """
        We collect, process and store the following publicly available information:

        - Portal Name
        - Article Title
        - Article URL
        - Author Name
        - Publish Date
        """),
        ("How we use this information", """
        We retain all the information that we collect for further use in following ways:

        - We will use the information to calculate metrics for <strong>the Media Monitor Dashboard ®</strong>
        - We may publish specific anti-Hindu article links, corresponding author and portal after suitable review to expose anti-Hindu content.
        - We may share the information we retain with our partner dharmic organizations in support of their advocacy efforts and research.
        """)
    ]
    
    for i in range(0, len(questions), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container():
                st.markdown(f"""
                <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 10px 0; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
                    <h3>{questions[i][0]}</h3>
                    <p>{questions[i][1]}</p>
                </div>
                """, unsafe_allow_html=True)
        
        if i + 1 < len(questions):
            with col2:
                with st.container():
                    st.markdown(f"""
                    <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 10px 0; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
                        <h3>{questions[i+1][0]}</h3>
                        <p>{questions[i+1][1]}</p>
                    </div>
                    """, unsafe_allow_html=True)