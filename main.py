import tweepy
import os
import geopy
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from geopy.geocoders import Nominatim

load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search_tweets, q="#flutter").items(100)

locations = {}

for tweet in tweets:
    location = tweet.user.location
    if location:
        if location in locations:
            locations[location] += 1
        else:
            locations[location] = 1

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

plt.scatter(longitudes, latitudes, s=counts, alpha=0.5)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Locations of Tweets on #flutter")
plt.savefig("locations.png")
plt.show()  