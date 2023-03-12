import tweepy, os
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search_tweets, q="#flutter").items(10)

for tweet in tweets:
    print("User: ", tweet.user.screen_name)
    print("Text: ", tweet.text)
    print("Retweets: ", tweet.retweet_count)
    print("Favorites: ", tweet.favorite_count)
    print("Created: ", tweet.created_at)
    print("Location: ", tweet.user.location)
    print("Source: ", tweet.source)
    print("\n")
