import tweepy
import requests

from config import c_key, c_secret, a_token, a_token_secret, b_token

# Twitter API key & secret

consumer_key = c_key
consumer_secret = c_secret

# Access token & secret

access_token = a_token
access_token_secret = a_token_secret

bearer_token = b_token

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# Generate and tweet an anecdote
def tweet_anecdote():
    # anecdote = get_anecdote("Write a short, humorous anecdote:")
    anecdote = "This is a test tweet"
    try:
        response = client.create_tweet(text=anecdote)
        print("Tweeted successfully! Response:", response)
    except Exception as e:
        print("Error in tweeting:", e)

# Schedule this function to run daily
tweet_anecdote()
