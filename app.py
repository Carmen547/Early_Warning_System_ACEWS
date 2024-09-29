# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Unique Page Configuration
st.set_page_config(page_title="Africa Conflict Early Warning System", page_icon="🌍")

# Sidebar - CSV upload
st.sidebar.title("Upload Conflict Tweets CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Load CSV Data Function
@st.cache_data
def load_data(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

if uploaded_file:
    df_tweets = load_data(uploaded_file)

    if df_tweets is not None:
        # Data Preview
        st.title('Africa Conflict Early Warning System 🌍')
        st.subheader('Preview of the Tweet Data')
        st.write(df_tweets.head(10))  # Show the first 10 rows of data

        # Filter Data
        st.subheader('Filter Tweet Data by Sentiment')
        sentiment_choice = st.radio("Select Sentiment", ['All', 'Positive', 'Neutral', 'Negative'])

        if sentiment_choice != 'All':
            df_filtered = df_tweets[df_tweets['sentiment'].str.lower() == sentiment_choice.lower()]
        else:
            df_filtered = df_tweets

        # Display Filtered Tweets
        st.write(f"Displaying {sentiment_choice} Tweets")
        st.dataframe(df_filtered[['created_at', 'cleaned_text', 'sentiment']])

        # Visualizing Sentiment Over Time
        st.subheader('Sentiment Analysis Over Time')
        df_tweets['created_at'] = pd.to_datetime(df_tweets['created_at'])
        daily_sentiment = df_tweets.groupby(df_tweets['created_at'].dt.date)['sentiment'].value_counts().unstack().fillna(0)

        st.line_chart(daily_sentiment)

        # Interactive Sentiment Pie Chart
        st.subheader('Sentiment Proportion')
        sentiment_count = df_tweets['sentiment'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(sentiment_count, labels=sentiment_count.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2"))
        ax.axis('equal')
        st.pyplot(fig)

    else:
        st.error("Error loading CSV file. Please check the format.")
else:
    st.info("Upload a CSV file to get started.")

