import streamlit as st

def run_page():
    st.title("Contact")

    # Custom CSS to override existing styles
    st.markdown("""
    <style>
    .contact-icon {
        width: 30px;
        margin-right: 10px;
        transform: none;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    Please send us an email should you have interest in collaborating with us or have any questions.

    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" class="contact-icon">
        <a href="mailto:hindumisia.ai@gmail.com">hindumisia.ai@gmail.com</a>
    </div>

    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" class="contact-icon">
        <a href="mailto:contact@hindumisia.ai">contact@hindumisia.ai</a>
    </div>

    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <img src="https://img.freepik.com/free-vector/new-2023-twitter-logo-x-icon-design_1017-45418.jpg?size=338&ext=jpg&ga=GA1.1.2008272138.1723593600&semt=ais_hybrid" class="contact-icon">
        <a href="https://x.com/hindumisia" target="_blank">@hindumisia</a>
    </div>

    <div style="display: flex; align-items: center;">
        <img src="https://static.vecteezy.com/system/resources/previews/014/414/683/non_2x/instagram-black-logo-on-transparent-background-free-vector.jpg" class="contact-icon">
        <a href="https://www.instagram.com/hindumisia.ai/" target="_blank">@hindumisia.ai</a>
    </div>
    """, unsafe_allow_html=True)