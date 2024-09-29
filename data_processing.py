import pandas as pd
from textblob import TextBlob

# Load the tweets data from CSV
df_tweets = pd.read_csv('data/conflict_tweets.csv')

# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)

# Apply sentiment analysis to the tweets
df_tweets['sentiment'] = df_tweets['text'].apply(analyze_sentiment)

# Save the results to a new CSV
df_tweets.to_csv('data/conflict_tweets_with_sentiment.csv', index=False)

