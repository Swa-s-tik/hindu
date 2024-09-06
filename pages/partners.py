import streamlit as st

def run_page():
    st.title("Partners")

    # Updated CSS for single row alignment
    st.markdown("""
    <style>
    # .partner-container {
    #     display: flex;
    #     flex-wrap: nowrap;
    #     justify-content: space-between;
    #     align-items: center;
    #     margin-top: 90px;
    # }
    .partner-container {
        display: flex;
        flex-wrap: nowrap;
        justify-content: space-between;
        align-items: center;
        margin-top: 3cm;
        padding-left: 1.5em; /* Adjust this value to align logos */
    }
    .partner-logo {
        width: 200px;
        height: 100px;
        object-fit: contain;
        margin: 0 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Partners logos in a single row
    st.markdown("""
    <div class="partner-container">
        <a href="http://www.indiafacts.org.in" target="_blank">
            <img src="https://www.indiafacts.org.in/wp-content/uploads/2020/08/INDIA-FACTS.png" class="partner-logo" alt="IndiaFacts">
        </a>
        <a href="https://myind.net/" target="_blank">
            <img src="https://myind.net/asset/images/logo.png" class="partner-logo" alt="MyInd">
        </a>
        <a href="http://hindupost.in" target="_blank">
            <img src="https://hindupost.in/wp-content/uploads/2021/07/Retina-Logo.png" class="partner-logo" alt="HinduPost">
        </a>
        <a href="https://smart4bharat.com/" target="_blank">
            <img src="https://media.licdn.com/dms/image/C4D0BAQGlf52T4UopwQ/company-logo_200_200/0/1662525306437?e=2147483647&v=beta&t=hENng2kMWtUtfEYmc0430O4DxXJGAVKQYtCACehNAXo" class="partner-logo" alt="Smart4Bharat">
        </a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_page()