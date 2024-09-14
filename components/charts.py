# components/charts.py
import plotly.graph_objects as go

def create_chart_title(base_title, date_range):
    return f'{base_title} {date_range}'.replace(' - ', ' and ')


def create_sentiment_pie_chart(df, date_range):
    sentiment_counts = df['sentiment_label'].value_counts()
    colors = {'Negative': '#FF0000', 'Neutral': '#A5A5A5', 'Positive': '#70AD47'}
    
    fig = go.Figure(data=[go.Pie(
        labels=sentiment_counts.index,
        values=sentiment_counts.values,
        marker=dict(colors=[colors[sent] for sent in sentiment_counts.index]),
        textinfo='label+percent',
        hovertemplate='Sentiment: %{label}<br># of Articles: %{value}<br>Percentage: %{percent}<extra></extra>'
    )])
    
    title = create_chart_title('Overall Tone', date_range)
    fig.update_layout(
        title=title,
        height=400,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False
    )
    fig.update_traces(texttemplate='%{label}: %{percent}')
    return fig

def create_stacked_portal_chart(df, date_range):
    portal_sentiment = df.groupby(['portal', 'sentiment_label']).size().unstack(fill_value=0)
    portal_sentiment['Total'] = portal_sentiment.sum(axis=1)
    portal_sentiment = portal_sentiment.sort_values('Total', ascending=False)
    
    fig = go.Figure()
    
    for sentiment in ['Negative', 'Neutral', 'Positive']:
        if sentiment in portal_sentiment.columns:
            fig.add_trace(go.Bar(
                y=portal_sentiment.index,
                x=portal_sentiment[sentiment],
                name=sentiment,
                orientation='h',
                marker=dict(color={'Negative': '#FF0000', 'Neutral': '#A5A5A5', 'Positive': '#70AD47'}[sentiment]),
                text=portal_sentiment[sentiment],
                textposition='auto',
                hovertemplate='Portal: %{y}<br>Sentiment: %{data.name}<br># of Articles: %{text}<extra></extra>'
            ))
    
    title = create_chart_title('Portal Statistics', date_range)
    fig.update_layout(
        barmode='stack',
        title=title,
        yaxis={'categoryorder': 'total ascending'},
        xaxis={'title': '# of Articles'},
        height=400,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False
    )
    return fig

def create_stacked_sentiment_graph(df, date_range):
    portal_sentiment = df.groupby('portal')['sentiment_label'].value_counts(normalize=True).unstack(fill_value=0)
    portal_sentiment = portal_sentiment.sort_values('Negative', ascending=False)
    # Check if 'Negative' column exists before sorting
    if 'Negative' in portal_sentiment.columns:
        portal_sentiment = portal_sentiment.sort_values('Negative', ascending=False)
    else:
        portal_sentiment = portal_sentiment.sort_index(ascending=True)  # Sort by index if 'Negative' doesn't exist
    
    fig = go.Figure()
    
    for sentiment, color in [('Negative', '#FF0000'), ('Neutral', '#A5A5A5'), ('Positive', '#70AD47')]:
        if sentiment in portal_sentiment.columns:
            fig.add_trace(go.Bar(
                y=portal_sentiment.index,
                x=-portal_sentiment[sentiment] if sentiment == 'Negative' else portal_sentiment[sentiment],
                name=sentiment,
                orientation='h',
                marker=dict(color=color),
                text=(portal_sentiment[sentiment] * 100).round(1).astype(str) + '%',
                textposition='inside',
                insidetextanchor='middle',
                hovertemplate='Portal: %{y}<br>Sentiment: %{data.name}<br>Percentage: %{text}<extra></extra>'
            ))
    
    title = create_chart_title('Tone Distribution', date_range)
    fig.update_layout(
        barmode='relative',
        title=title,
        yaxis={'categoryorder': 'total descending', 'title': ''},
        xaxis={'title': '', 'tickformat': '', 'range': [-1, 1], 'showticklabels': False},
        height=400,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False
    )
    return fig

def create_sentiment_trend(df, date_range):
    df = df.copy()  # Ensure df is a copy
    df.loc[:, 'date'] = df['published_date'].dt.date
    sentiment_over_time = df.groupby(['date', 'sentiment_label']).size().unstack(fill_value=0).reset_index()
    
    fig = go.Figure()
    
    for sentiment, color in [('Negative', 'red'), ('Neutral', 'grey'), ('Positive', 'green')]:
        if sentiment in sentiment_over_time.columns:
            fig.add_trace(go.Scatter(
                x=sentiment_over_time['date'],
                y=sentiment_over_time[sentiment],
                mode='lines',
                name=sentiment,
                line=dict(color=color)
            ))
    
    title = create_chart_title('Trends', date_range)
    fig.update_layout(
        title=title,
        xaxis=dict(
            title=" ",
            tickformat='%d %b %Y',
            dtick='D1'
        ),
        yaxis=dict(title="# of Articles"),
        height=400,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False,
        hovermode="x unified"
    )
    
    fig.update_traces(
        hovertemplate='Date: %{x|%d %b %Y}<br>Sentiment: %{data.name}<br># of Articles: %{y}<extra></extra>'
    )

    total_articles = sentiment_over_time.iloc[:, 1:].sum(axis=1)
    fig.add_trace(go.Scatter(
        x=sentiment_over_time['date'],
        y=total_articles,
        mode='lines',
        name='Total',
        line=dict(color='#87CEEB')
    ))
    return fig