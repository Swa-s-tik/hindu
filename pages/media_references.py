import streamlit as st

def run_page():
    st.title("Media References")

    st.markdown("""
    <style>
    .reference-container {
        display: flex;
        gap: 20px;
        margin-bottom: 20px;
    }
    .reference-item {
        flex: 1;
        display: flex;
        align-items: center;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .reference-image {
        width: 100px;
        height: 100px;
        object-fit: contain;
        margin-right: 15px;
        transform: none !important;
    }
    .reference-content {
        flex-grow: 1;
    }
    .reference-content h3 {
        margin: 0;
        font-size: 1.1em;
    }
    .reference-content p {
        margin: 5px 0 0;
        font-size: 0.9em;
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

    st.header("Articles", anchor=False)

    articles = [
        {
            "title": "An AI-Based Approach To Monitor, Expose, And Counter Anti-Hindu Hate",
            "url": "https://swarajyamag.com/tech/an-ai-based-approach-to-monitor-expose-and-counter-anti-hindu-hate",
            "image": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Swarajya_logo.png"
        },
        {
            "title": '"This Month in Hinduphobia" Series sourced from hindumisia.ai platform',
            "url": "https://www.indiafacts.org.in/category/hinduphobia/",
            "image": "https://www.indiafacts.org.in/wp-content/uploads/2020/08/INDIA-FACTS.png"
        },
        {
            "title": "Monthly Anti-Hindu Scorecards",
            "url": "https://myind.net/Home/authorArchives/2736",
            "image": "https://myind.net/asset/images/logo.png"
        },
        {
            "title": "The Global Anti-Hindu Report for 2022",
            "url": "https://organiser.org/2023/06/10/178261/world/hindumisia-ai-report-2022-ai-analyses-anti-hindu-ecosystem-lists-50-twitter-accounts-propagating-anti-hindu-sentiment/",
            "image": "https://organiser.org/wp-content/uploads/2022/07/organiser-logo@2x.png"
        }
    ]

    for i in range(0, len(articles), 2):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="reference-item">
                <img src="{articles[i]['image']}" class="reference-image">
                <div class="reference-content">
                    <h3><a href="{articles[i]['url']}">{articles[i]['title']}</a></h3>
                </div>
            </div>
            """, unsafe_allow_html=True)
        if i + 1 < len(articles):
            with col2:
                st.markdown(f"""
                <div class="reference-item">
                    <img src="{articles[i+1]['image']}" class="reference-image">
                    <div class="reference-content">
                        <h3><a href="{articles[i+1]['url']}">{articles[i+1]['title']}</a></h3>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.header("Webinars", anchor=False)

    webinars = [
        {
            "title": "Hindumisia.ai: The Global Anti-Hindu Scorecard",
            "url": "https://www.youtube.com/watch?v=fNsO4pf_6Jg",
            "image": "https://via.placeholder.com/100?text=Carvaka+Podcast",
            "source": "The Carvaka Podcast"
        },
        {
            "title": "The Need to Call out Anti-Hindu Hate in the Media",
            "url": "https://www.youtube.com/watch?v=A8rW2QZzjjs",
            "image": "https://www.pgurus.com/wp-content/uploads/2017/11/Pgurus_03_500px.png",
            "source": "PGurus"
        },
        {
            "title": "Hindumisia is Real",
            "url": "https://www.youtube.com/watch?v=zURU_tZEqxo",
            "image": "https://via.placeholder.com/100?text=Jaipur+Dialogues",
            "source": "The Jaipur Dialogues"
        },
        {
            "title": "Psychological Impact of Colonialism",
            "url": "https://www.youtube.com/watch?v=MpKHW91BS5M",
            "image": "https://stophindudvesha.org/wp-content/uploads/2023/11/logo16x9.jpg",
            "source": "Stop Hindu Dvesha"
        }
    ]

    for i in range(0, len(webinars), 2):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="reference-item">
                <img src="{webinars[i]['image']}" class="reference-image">
                <div class="reference-content">
                    <h3><a href="{webinars[i]['url']}">{webinars[i]['title']}</a></h3>
                    <p>{webinars[i]['source']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        if i + 1 < len(webinars):
            with col2:
                st.markdown(f"""
                <div class="reference-item">
                    <img src="{webinars[i+1]['image']}" class="reference-image">
                    <div class="reference-content">
                        <h3><a href="{webinars[i+1]['url']}">{webinars[i+1]['title']}</a></h3>
                        <p>{webinars[i+1]['source']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_page()