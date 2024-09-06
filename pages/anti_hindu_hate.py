import streamlit as st

def run_page():
    st.markdown("# Anti-Hindu Hate", unsafe_allow_html=True)
    
    questions = [
        ("What is Anti-Hindu hate?", """
        Anti-Hindu hate is the anti-Hindu sentiment that advances, amplifies, and articulates
        hatred against Hindus and Hinduism. This is a toxic global phenomenon influenced by
        the legacies of the past.

        Anti-Hindu hate refers to bias, discrimination, or prejudice directed towards
        individuals or communities based on their association with Hinduism, one of the
        world's oldest and most diverse religions. This form of hate can manifest in various
        ways, including verbal attacks, physical violence and the dissemination of harmful
        stereotypes and misinformation. It targets the core aspects of Hindu identity, practices,
        and beliefs, aiming to marginalize or vilify those who adhere to this faith.
        """),
        ("What is the difference between Hinduphobia, Hindumisia, Hindudvesha?", """
        In principle, there's no difference. 'Phobia' stands for fear, 'Misia' stands for hatred and
        'dvesha' is a sanskrit terminology for hate. They all refer to anti-Hindu hate.

        While those who use the terms are bound by their own conviction, the difference has
        negligible impact on the dharmic ecosystem's ability to counter anti-Hindu Hate.
        "Hindumisia" is here to stay, and so are the terms "Hinduphobia" and "Hindudvesha".
        hindumisia.<span style='color: #FF9934;'>ai</span> welcomes the use of all these terms. All these terms will have to co-exist.
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