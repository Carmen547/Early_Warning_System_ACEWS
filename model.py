import pandas as pd

# Load the tweets data with sentiment from CSV
df_tweets = pd.read_csv('data/conflict_tweets_with_sentiment.csv')

# Example function to analyze the data (like getting average sentiment)
def analyze_sentiment_distribution(df):
    average_sentiment = df['sentiment'].mean()
    print(f"Average Sentiment Polarity: {average_sentiment}")

# Call the function to analyze sentiment
analyze_sentiment_distribution(df_tweets)

