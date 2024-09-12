# utils/helpers.py
import numpy as np
def format_date(date):
    return date.strftime('%d %b %Y')

# Function to safely convert numpy types to Python types
def safe_convert(value):
    if isinstance(value, np.integer):
        return int(value)
    elif isinstance(value, np.floating):
        return float(value)
    return value

def get_headlines(df, date):
    daily_data = df[df['published_date'].dt.date == date]
    columns = ['portal', 'published_date', 'author', 'headline', 'url_link', 'sentiment_label']
    return daily_data[columns]

def format_date_range(start_date, end_date):
    return f"{format_date(start_date)} and {format_date(end_date)}".replace('-', 'and')
