import streamlit as st

def run_page():
    st.markdown("<h1 style='font-size: calc(1.8rem + 1.8vw);'>About hindumisia.<span style='color: #FF9934;'>ai</span></h1>", unsafe_allow_html=True)

    questions = [
        ("What is hindumisia.<span style='color: #FF9934;'>ai</span>?", """
        hindumisia.<span style='color: #FF9934;'>ai</span> is a platform dedicated to monitoring and countering anti-Hindu sentiment, 
        utilizing the evolving fields of Artificial Intelligence and Natural Language Processing. 
        The platform pioneered the concept of AI-based approach to detecting anti-Hindu hate sourcing 
        tweets from X realtime and visualizing them in The Global Anti-Hindu Scorecard ®.  The 
        platform shifted its focus in April 2024 to tracking  media sentiments across various media 
        outlets with the launch of Media Sentiment Scorecard ® (briefly called Media Monitor Dashboard). 
                    
        The AI-based approach was based on an NLP model that has been greatly simplified and repurposed 
        for use with media portals.
        """),
        ("How does the tool work?", """
        The platform functions by offering periodical statistics and visualizations of general sentiments, 
        presenting an overview of  the wider media environment using Media Sentiment Scorecard ®. Differing 
        from its predecessor, the updated version focuses on visualizing general sentiment for the time being. 

        The analysis of anti-Hindu sentiments is conducted using a custom-developed, streamlined NLP model, 
        and the insights will be incorporated into our routine reports. As the  model matures, the platform 
        will be updated to include anti-Hindu sentiments in the Media Sentiment Scorecard ®  online in the 
        future.
        """),
        ("Will additional portals be included in the future?", """
        Yes. There are over two dozen media outlets/portals to be included in the analysis. Besides, there are plans to 
        offer API access to the AI model for use by select dharmic organizations.
        """),
        ("Do you store all articles?", """
        No, we do not store articles that we scan from portals. We only read the URL of the article and use the title 
        to detect sentiments, for our reporting needs. URL of the article and the Article Title 
        is stored for reference and reporting purposes.
        """),
        ("How is anti-Hindu hate detected?", """
        Anti-Hindu hate is detected using an Artificial Intelligence model and NLP techniques.
         
        """),        
        ("Is there a way to access all the stored data?", """
        There's no public access to the stored dataset. They are meant for hindumisia.<span style='color: #FF9934;'>ai</span> use only.
         
        """),
        # ... other questions ...
    ]

    for i in range(0, len(questions), 2):
        col1, col2 = st.columns([1, 1])

        with col1:
            with st.expander(questions[i][0]):
                st.markdown(questions[i][1], unsafe_allow_html=True)

        if i + 1 < len(questions):
            with col2:
                with st.expander(questions[i+1][0]):
                    st.markdown(questions[i+1][1], unsafe_allow_html=True)