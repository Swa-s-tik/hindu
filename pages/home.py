# pages/home.py
import calendar
from tkinter import Image
import pandas as pd
import streamlit as st
from components import layout, charts, metrics
from ml import data_processing
from utils import helpers
from datetime import datetime, timedelta

def get_daily_stats(df, date):
    daily_data = df[df['published_date'].dt.date == date]
    total_count = len(daily_data)
    sentiment_counts = daily_data['sentiment_label'].value_counts()
    return total_count, sentiment_counts

def run_page():
    df = data_processing.load_data()
    view, selected_portal = layout.create_responsive_layout(df)
    
    if view == "Daily":
        main_dashboard(df)
    elif view == "Monthly":
        monthly_dashboard(df)
    else:
        range_dashboard(df)

def main_dashboard(df):
    # Get the minimum and maximum dates from the DataFrame
    min_date = df['published_date'].min().date()
    # max_date = df['published_date'].max().date()
    max_date = df[df['published_date'] <= pd.Timestamp('today') - pd.Timedelta(days=1)]['published_date'].max().date()


    # Date and portal selection in the same row
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="selection-title">Select a Date</p>', unsafe_allow_html=True)
        selected_date = st.date_input("Select a Date", min_value=min_date, max_value=max_date, value=max_date, format="DD/MM/YYYY", label_visibility="collapsed")
    with col2:
        st.markdown('<p class="selection-title">Select Portal</p>', unsafe_allow_html=True)
        portals = ['All'] + sorted(df['portal'].unique().tolist())
        selected_portal = st.selectbox("Select Portal", portals, label_visibility="collapsed")

    if selected_portal != 'All':
        df = df[df['portal'] == selected_portal]

    if selected_date:
        # Get stats for selected date and previous date
        current_total, current_sentiments = get_daily_stats(df, selected_date)
        previous_date = selected_date - timedelta(days=1)
        previous_total, previous_sentiments = get_daily_stats(df, previous_date)

        if current_total == 0:
            st.warning("No articles found for this selected date. Please select a different date.")
        else:
            # Display metrics
            col1, col2, col3, col4 = st.columns(4)

            metric_data = [
                ("Total Articles", current_total, current_total - previous_total, "total-articles"),
                ("Negative", current_sentiments.get('Negative', 0), current_sentiments.get('Negative', 0) - previous_sentiments.get('Negative', 0), "negative-articles"),
                ("Neutral", current_sentiments.get('Neutral', 0), current_sentiments.get('Neutral', 0) - previous_sentiments.get('Neutral', 0), "neutral-articles"),
                ("Positive", current_sentiments.get('Positive', 0), current_sentiments.get('Positive', 0) - previous_sentiments.get('Positive', 0), "positive-articles")
            ]

            for col, (label, value, delta, class_name) in zip([col1, col2, col3, col4], metric_data):
                with col:
                    delta_class = "delta-positive" if delta > 0 else "delta-negative"
                    delta_symbol = "▲" if delta > 0 else "▼"
                    st.markdown(f"""
                    <div class="metric-box {class_name}">
                        <div class="metric-header">{label}</div>
                        <div class="metric-value">{helpers.safe_convert(value)}</div>
                        <div class="metric-separator"></div>
                        <div class="metric-delta {delta_class}">{delta_symbol} {abs(helpers.safe_convert(delta))}</div>
                        <div class="metric-subtext">From Previous Day</div>
                        <div class="metric-equation">{'=' if label == 'Total Articles' else '+' if label != 'Positive' else ''}</div>
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

            selected_date_str = helpers.format_date(selected_date)

            # Use a single row with 3 equal columns
            col1, col2, col3 = st.columns(3)

            with col1:
                pie_chart = charts.create_sentiment_pie_chart(df[df['published_date'].dt.date == selected_date], f"for {selected_date_str}")
                st.plotly_chart(pie_chart, use_container_width=True, config={'displayModeBar': False})

            with col2:
                portal_chart = charts.create_stacked_portal_chart(df[df['published_date'].dt.date == selected_date], f"for {selected_date_str}")
                st.plotly_chart(portal_chart, use_container_width=True, config={'displayModeBar': False})

            with col3:
                sentiment_distribution = charts.create_stacked_sentiment_graph(df[df['published_date'].dt.date == selected_date], f"for {selected_date_str}")
                st.plotly_chart(sentiment_distribution, use_container_width=True, config={'displayModeBar': False})

            # Display headlines
            st.subheader(f"Headlines for {selected_date.strftime('%d-%b-%Y')}")

            headlines = helpers.get_headlines(df, selected_date)

            # Add filter and search options
            col1, col2 = st.columns(2)
            with col1:
                search_query = st.text_input("Search headlines", placeholder="Enter keywords and press Enter to search")
            with col2:
                sentiment_filter = st.selectbox("Filter headlines by sentiment", ["All", "Negative", "Neutral", "Positive"])

            # Apply filters
            if search_query:
                headlines = headlines[headlines['headline'].str.contains(search_query, case=False)]
            if sentiment_filter != "All":
                headlines = headlines[headlines['sentiment_label'] == sentiment_filter]

            headlines = headlines.reset_index(drop=True)
            headlines.index = headlines.index + 1

            # Create clickable links
            if 'url_link' in headlines.columns:
                headlines.loc[:, 'url_link'] = headlines['url_link'].apply(lambda x: f'<a href="{x}" target="_blank">Read More</a>')
            elif 'url' in headlines.columns:
                headlines['url'] = headlines['url'].apply(lambda x: f'<a href="{x}" target="_blank">Read More</a>')

            # Apply sentiment color styling
            headlines.loc[:, 'sentiment_label'] = headlines['sentiment_label'].apply(
                lambda x: f'<span style="color: {"green" if x == "Positive" else "red" if x == "Negative" else "gray"}">{x}</span>'
            )

            # Rename columns
            headlines.columns = ['Portal', 'Published Date', 'Author', 'Headline', 'URL Link', 'Sentiment']

            # Display the styled table with pagination
            if len(headlines) > 10:
                if 'show_all' not in st.session_state:
                    st.session_state.show_all = False

                if st.session_state.show_all:
                    st.markdown(headlines.to_html(escape=False, index=True), unsafe_allow_html=True)
                    if st.button("Show Less"):
                        st.session_state.show_all = False
                        st.rerun()
                else:
                    st.markdown(headlines.head(10).to_html(escape=False, index=True), unsafe_allow_html=True)
                    if st.button("Show more"):
                        st.session_state.show_all = True
                        st.rerun()
            else:
                st.markdown(headlines.to_html(escape=False, index=True), unsafe_allow_html=True)


def monthly_dashboard(df):
    # Get the minimum and maximum dates from the DataFrame
    min_date = df['published_date'].min().date()
    # max_date = df['published_date'].max().date()
    max_date = df[df['published_date'] <= pd.Timestamp('today') - pd.Timedelta(days=1)]['published_date'].max().date()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="selection-title">Select Month</p>', unsafe_allow_html=True)
        month_year_options = [d.strftime("%B %Y") for d in pd.date_range(start=min_date, end=max_date, freq='MS')]
        default_month = max_date.strftime("%B %Y")
        selected_month_year = st.selectbox("Select Month", month_year_options, index=month_year_options.index(default_month), key="select_month_year_monthly", label_visibility="collapsed")

    with col2:
        st.markdown('<p class="selection-title">Select Portal</p>', unsafe_allow_html=True)
        portals = ['All'] + sorted(df['portal'].unique().tolist())
        selected_portal = st.selectbox("Select Portal", portals, key="portal_selector_monthly", label_visibility="collapsed")
     
    if selected_portal != 'All':
        df = df[df['portal'] == selected_portal]

    if selected_month_year != "Select Month":
        month, year = selected_month_year.split()
        month_num = list(calendar.month_name).index(month)
        start_date = pd.to_datetime(f"01-{datetime.strptime(month, '%B').month:02d}-{year}", format='%d-%m-%Y')
        end_date = start_date + pd.offsets.MonthEnd(0)
        mask = (df['published_date'].dt.date >= start_date.date()) & (df['published_date'].dt.date <= end_date.date())
        filtered_df = df.loc[mask]
        date_range_str = selected_month_year

        # Calculate total articles and sentiment counts
        total_articles = len(filtered_df)
        sentiment_counts = filtered_df['sentiment_label'].value_counts()

        # Display metrics
        col1, col2, col3, col4 = st.columns(4)

        metric_data = [
            ("Total Articles", total_articles, "For Selected Month", "total-articles"),
            ("Negative", sentiment_counts.get('Negative', 0), "For Selected Month", "negative-articles"),
            ("Neutral", sentiment_counts.get('Neutral', 0), "For Selected Month", "neutral-articles"),
            ("Positive", sentiment_counts.get('Positive', 0), "For Selected Month", "positive-articles")
        ]

        for col, (label, value, subtext, class_name) in zip([col1, col2, col3, col4], metric_data):
            with col:
                st.markdown(f"""
                <div class="metric-box {class_name}">
                    <div class="metric-header">{label}</div>
                    <div class="metric-value">{helpers.safe_convert(value)}</div>
                    <div class="metric-separator"></div>
                    <div class="metric-subtext">{subtext}</div>
                    <div class="metric-equation">{'=' if label == 'Total Articles' else '+' if label != 'Positive' else ''}</div>
                </div>
                """, unsafe_allow_html=True)

        selected_month_str = selected_month_year

        # Create and display charts
        col1, col2 = st.columns(2)

        with col1:
            pie_chart = charts.create_sentiment_pie_chart(filtered_df, f"for {selected_month_str}")
            st.plotly_chart(pie_chart, use_container_width=True, config={'displayModeBar': False})

        with col2:
            portal_chart = charts.create_stacked_portal_chart(filtered_df, f"for {selected_month_str}")
            st.plotly_chart(portal_chart, use_container_width=True, config={'displayModeBar': False})

        col3, col4 = st.columns(2)

        with col3:
            trend_chart = charts.create_sentiment_trend(filtered_df, f"for {selected_month_str}")
            st.plotly_chart(trend_chart, use_container_width=True, config={'displayModeBar': False})

        with col4:
            sentiment_distribution = charts.create_stacked_sentiment_graph(filtered_df, f"for {selected_month_str}")
            st.plotly_chart(sentiment_distribution, use_container_width=True, config={'displayModeBar': False})

        # Display headlines
        st.subheader(f"Headlines for {date_range_str}")
        
        # Search and filter
        col1, col2 = st.columns(2)
        with col1:
            search_query = st.text_input("Search headlines", placeholder="Enter keywords and press Enter to search", key="headline_search_monthly")
        with col2:
            sentiment_filter = st.selectbox("Filter by Sentiment", ["All", "Positive", "Neutral", "Negative"], key="sentiment_filter_monthly")

        # Apply filters
        if search_query:
            filtered_df = filtered_df[filtered_df['headline'].str.contains(search_query, case=False)]
        if sentiment_filter != "All":
            filtered_df = filtered_df[filtered_df['sentiment_label'] == sentiment_filter]

        # Display headlines
        headlines = filtered_df[['portal', 'published_date', 'author', 'headline', 'url_link', 'sentiment_label']]
        headlines.loc[:, 'url_link'] = headlines['url_link'].apply(lambda x: f'<a href="{x}" target="_blank">Read More</a>')
        headlines.loc[:, 'sentiment_label'] = headlines['sentiment_label'].apply(
            lambda x: f'<span style="color: {"green" if x == "Positive" else "red" if x == "Negative" else "gray"}">{x}</span>'
        )
        headlines.columns = ['Portal', 'Published Date', 'Author', 'Headline', 'URL Link', 'Sentiment']

        if len(headlines) > 10:
            if 'show_all_monthly' not in st.session_state:
                st.session_state.show_all_monthly = False

            if st.session_state.show_all_monthly:
                st.markdown(headlines.to_html(escape=False, index=False), unsafe_allow_html=True)
                if st.button("Show Less", key="show_less_monthly"):
                    st.session_state.show_all_monthly = False
                    st.rerun()
            else:
                st.markdown(headlines.head(10).to_html(escape=False, index=False), unsafe_allow_html=True)
                if st.button("Show more", key="show_more_monthly"):
                    st.session_state.show_all_monthly = True
                    st.rerun()
        else:
            st.markdown(headlines.to_html(escape=False, index=False), unsafe_allow_html=True)


def range_dashboard(df):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<p class="selection-title">Start Date</p>', unsafe_allow_html=True)
        start_date = st.date_input("Start Date", value=None, min_value=df['published_date'].min().date(), max_value=df['published_date'].max().date(), format="DD/MM/YYYY", key="start_date", label_visibility="collapsed")
    with col2:
        st.markdown('<p class="selection-title">End Date</p>', unsafe_allow_html=True)
        end_date = st.date_input("End Date", value=None, min_value=df['published_date'].min().date(), max_value=df['published_date'].max().date(), format="DD/MM/YYYY", key="end_date", label_visibility="collapsed")
    with col3:
        st.markdown('<p class="selection-title">Select Portal</p>', unsafe_allow_html=True)
        portals = ['All'] + sorted(df['portal'].unique().tolist())
        selected_portal = st.selectbox("Select Portal", portals, key="portal_selector_range", label_visibility="collapsed")
    
    if selected_portal != 'All':
        df = df[df['portal'] == selected_portal]

    if start_date and end_date:
        mask = (df['published_date'].dt.date >= start_date) & (df['published_date'].dt.date <= end_date)
        filtered_df = df.loc[mask]
        date_range_str = helpers.format_date_range(start_date, end_date)
        # st.write(f"Debug: date_range_str = {date_range_str}") #to check date pattern

        # Calculate total articles and sentiment counts
        total_articles = len(filtered_df)
        sentiment_counts = filtered_df['sentiment_label'].value_counts()

        # Display metrics
        col1, col2, col3, col4 = st.columns(4)

        metric_data = [
            ("Total Articles", total_articles, "For Selected Period", "total-articles"),
            ("Negative", sentiment_counts.get('Negative', 0), "For Selected Period", "negative-articles"),
            ("Neutral", sentiment_counts.get('Neutral', 0), "For Selected Period", "neutral-articles"),
            ("Positive", sentiment_counts.get('Positive', 0), "For Selected Period", "positive-articles")
        ]

        for col, (label, value, subtext, class_name) in zip([col1, col2, col3, col4], metric_data):
            with col:
                st.markdown(f"""
                <div class="metric-box {class_name}">
                    <div class="metric-header">{label}</div>
                    <div class="metric-value">{helpers.safe_convert(value)}</div>
                    <div class="metric-separator"></div>
                    <div class="metric-subtext">{subtext}</div>
                    <div class="metric-equation">{'=' if label == 'Total Articles' else '+' if label != 'Positive' else ''}</div>
                </div>
                """, unsafe_allow_html=True)

        date_range_str = f"{helpers.format_date(start_date)} - {helpers.format_date(end_date)}"

        # Create and display charts
        col1, col2 = st.columns(2)

        with col1:
            pie_chart = charts.create_sentiment_pie_chart(filtered_df, f"between {date_range_str}")
            st.plotly_chart(pie_chart, use_container_width=True, config={'displayModeBar': False})

        with col2:
            portal_chart = charts.create_stacked_portal_chart(filtered_df, f"between {date_range_str}")
            st.plotly_chart(portal_chart, use_container_width=True, config={'displayModeBar': False})

        col3, col4 = st.columns(2)

        with col3:
            trend_chart = charts.create_sentiment_trend(filtered_df, f"between {date_range_str}")
            st.plotly_chart(trend_chart, use_container_width=True, config={'displayModeBar': False})

        with col4:
            sentiment_distribution = charts.create_stacked_sentiment_graph(filtered_df, f"between {date_range_str}")
            st.plotly_chart(sentiment_distribution, use_container_width=True, config={'displayModeBar': False})

        # Display headlines
        st.subheader(f"Headlines between {date_range_str}")
        
        # Search and filter
        col1, col2 = st.columns(2)
        with col1:
            search_query = st.text_input("Search headlines", placeholder="Enter keywords and press Enter to search", key="headline_search_range")
        with col2:
            sentiment_filter = st.selectbox("Filter by Sentiment", ["All", "Positive", "Neutral", "Negative"], key="sentiment_filter_range")

        # Apply filters
        if search_query:
            filtered_df = filtered_df[filtered_df['headline'].str.contains(search_query, case=False)]
        if sentiment_filter != "All":
            filtered_df = filtered_df[filtered_df['sentiment_label'] == sentiment_filter]

        # Display headlines
        headlines = filtered_df[['portal', 'published_date', 'author', 'headline', 'url_link', 'sentiment_label']]
        headlines.loc[:, 'url_link'] = headlines['url_link'].apply(lambda x: f'<a href="{x}" target="_blank">Read More</a>')
        headlines.loc[:, 'sentiment_label'] = headlines['sentiment_label'].apply(
            lambda x: f'<span style="color: {"green" if x == "Positive" else "red" if x == "Negative" else "gray"}">{x}</span>'
        )
        headlines.columns = ['Portal', 'Published Date', 'Author', 'Headline', 'URL Link', 'Sentiment']

        if len(headlines) > 10:
            if 'show_all_range' not in st.session_state:
                st.session_state.show_all_range = False

            if st.session_state.show_all_range:
                st.markdown(headlines.to_html(escape=False, index=False), unsafe_allow_html=True)
                if st.button("Show Less", key="show_less_range"):
                    st.session_state.show_all_range = False
                    st.rerun()
            else:
                st.markdown(headlines.head(10).to_html(escape=False, index=False), unsafe_allow_html=True)
                if st.button("Show more", key="show_more_range"):
                    st.session_state.show_all_range = True
                    st.rerun()
        else:
            st.markdown(headlines.to_html(escape=False, index=False), unsafe_allow_html=True)
