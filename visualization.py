import pandas as pd
import matplotlib.pyplot as plt

# Load the tweets data with sentiment from CSV
df_tweets = pd.read_csv('data/conflict_tweets_with_sentiment.csv')

# Example visualization: Plotting sentiment distribution
def plot_sentiment_distribution(df):
    plt.figure(figsize=(10, 6))
    df['sentiment'].hist(bins=30)
    plt.title('Sentiment Distribution of Tweets')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# Call the function to plot the sentiment distribution
plot_sentiment_distribution(df_tweets)

