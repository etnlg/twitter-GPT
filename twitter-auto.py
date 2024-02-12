try:
    import tweepy
    from openai import OpenAI

    from config import c_key, c_secret, a_token, a_token_secret, b_token, openAI_key

    # Twitter API key & secret

    consumer_key = c_key
    consumer_secret = c_secret

    # Access token & secret

    access_token = a_token
    access_token_secret = a_token_secret

    bearer_token = b_token


    client_twitter = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

    # Generate and tweet an anecdote
    def tweet_anecdote(anecdote):
        # anecdote = get_anecdote("Write a short, humorous anecdote:")
        try:
            response = client_twitter.create_tweet(text=anecdote)
            print("Tweeted successfully! Response:", response)
        except Exception as e:
            print("Error in tweeting:", e)

    # GPT-4 API call

    gpt_key = openAI_key

    client_gpt = OpenAI(api_key = openAI_key)

    completion = client_gpt.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a passionate teacher of geopolitics and history, and you have a twitter account where you share daily statistics and anectodes about the world."},
        {"role": "user", "content": "Write a tweet."},
    ]
    )
    response = completion.choices[0].message

    # Schedule this function to run daily
    tweet_anecdote(response.content)
except Exception as e:
    # This block will execute if any exception is raised in the try block
    print(f"An error occurred: {e}")
    with open("Users/etienneleguay/Desktop/log-cron.txt", "a") as file:
        file.write(f"An error occurred: {e}\n")
