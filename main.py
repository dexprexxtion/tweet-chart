import tweepy
import os
import geopy
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from geopy.geocoders import Nominatim

version = 0.1
number_of_tweets = 100

load_dotenv()

print("version", version)
print("Keys loaded successfully.")

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)
print("Authenticated with OAuth Twitter API.")

print("Searching for tweets...")
tweets = tweepy.Cursor(api.search_tweets, q="#flutter").items(number_of_tweets)
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

geolocator = Nominatim(user_agent="tweet_chart")
latitudes = []
longitudes = []
counts = []
for location in locations:
    try:
        location_info = geolocator.geocode(location)
        if location_info:
            latitudes.append(location_info.latitude)
            longitudes.append(location_info.longitude)
            counts.append(locations[location])
    except:
        pass

print("Geolocator job done.")
print("Creating ScatterPlot")

plt.scatter(longitudes, latitudes, s=counts, alpha=0.5)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Locations of Tweets on #flutter")
plt.savefig("locations.png")
plt.show()  

print("Finished.")