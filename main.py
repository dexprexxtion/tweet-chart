import tweepy
import os
import geopy
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from geopy.geocoders import Nominatim

version = 0.1
number_of_tweets = 50
hashtag = "#flutter"

load_dotenv()

print("version", version)
print("Keys loaded successfully.")

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)
print("Authenticated with OAuth Twitter API.")

print("Searching for tweets...")
tweets = tweepy.Cursor(api.search_tweets, q=hashtag).items(number_of_tweets)
print("Fetched ", number_of_tweets," tweets.")


locations = {}

for tweet in tweets:
    location = tweet.user.location
    if location:
        if location in locations:
            locations[location] += 1
        else:
            locations[location] = 1

print("Locations dictionary loaded successfully.")

fig, ax = plt.subplots()
ax.bar(locations.keys(), locations.values())
plt.xticks(rotation=90)
plt.xlabel("Location")
plt.ylabel("Number of Tweets")
plt.title("Locations of Tweets on #flutter")
plt.tight_layout()
plt.savefig("locations.png")
plt.show()
print("Finished.")