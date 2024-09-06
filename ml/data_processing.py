# ml/data_processing.py
import pandas as pd

def load_data():
    df = pd.read_csv('news_unique.csv')
    df['published_date'] = pd.to_datetime(df['published_date'], format='%d-%m-%Y')
    return df

def filter_dataframe(df, view, selected_portal):
    # Your dataframe filtering logic here
    pass