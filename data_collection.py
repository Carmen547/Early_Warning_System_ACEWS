import tweepy
import pandas as pd

# Define your Twitter API credentials here
consumer_key = 'your_consumer_key'  # Replace with your actual consumer key
consumer_secret = 'your_consumer_secret'  # Replace with your actual consumer secret
access_token = 'your_access_token'  # Replace with your actual access token
access_token_secret = 'your_access_token_secret'  # Replace with your actual access token secret

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Define a search query and date range
search_query = '#conflict OR #war OR #protest -filter:retweets'
date_since = "2024-01-01"
date_until = "2024-12-31"

# Collect tweets
tweets = tweepy.Cursor(api.search,
                       q=search_query,
                       lang="en",
                       since=date_since,
                       until=date_until).items(1000)

# Store tweets in a DataFrame
tweets_data = [{'text': tweet.text, 'created_at': tweet.created_at} for tweet in tweets]
df_tweets = pd.DataFrame(tweets_data)

# Save to CSV
df_tweets.to_csv('data/conflict_tweets.csv', index=False)

