import tweepy
import requests

# Twitter API key & secret

consumer_key = "5aNJgxlHDxwznk3pd9BuN6t01"
consumer_secret = "k6Xe7LhwL9gmhDVVaCVNtIok6V7KgGBdMQHDUDOub7Bwg2ICTL"

# Access token & secret

access_token = "4657921942-HF3yuf9ndtssiuw6pcWkWkGlGzFIbT04xdtcdFv"
access_token_secret = "UzeIBKvAJfKwzWIwIrAXj1LPe71Z36bYqWHyo5q7AgUgv"

bearer_token = "AAAAAAAAAAAAAAAAAAAAAOWcrgEAAAAAjKd7%2FDTDeVOUZ41NJuwfAzvwmpI%3DcTgRKvdq3D6Haqjg91gNDSbBbwYo5hCw75AAvCOUbC3ipiYISa"

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# GPT-4 API call
# def get_anecdote(prompt):
#     response = requests.post(
#         "GPT-4_API_ENDPOINT",
#         headers={"Authorization": f"Bearer YOUR_GPT4_API_KEY"},
#         json={"prompt": prompt, "max_tokens": 200}
#     )
#     return response.json().get('choices')[0].get('text').strip()

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
