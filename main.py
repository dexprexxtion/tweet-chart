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

print("version", version) #status
print("Keys loaded successfully.") #status

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

print("Authenticating with OAuth...") #status

api = tweepy.API(auth)
print("Authenticated with OAuth Twitter API.") #status

print("Searching for tweets...") #status
tweets = tweepy.Cursor(api.search_tweets, q=hashtag).items(number_of_tweets)
print("Fetched ", number_of_tweets," tweets.") #status


locations = {}

print("Loading locations dictionary...") # status
for tweet in tweets:
    location = tweet.user.location
    if location:
        if location in locations:
            locations[location] += 1
        else:
            locations[location] = 1

print("Locations dictionary loaded successfully.") #status

print("Using geolocator to obtain Latitudes and Longitudes of user locations...") #status
geolocator = Nominatim(user_agent="my_application") 
latitudes = []
longitudes = []
counts = []
print("Starting geolocator...") #status
for location in locations:
    try:
        location_info = geolocator.geocode(location)
        if location_info:
            latitudes.append(location_info.latitude)
            longitudes.append(location_info.longitude)
            counts.append(locations[location])
    except:
        pass
print("Geolocator coordinates obtained successfully.") #status

print("Creating ScatterPlot...") #status
plt.scatter(longitudes, latitudes, s=counts, alpha=0.5)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Locations of Tweets on #flutter")
print("Saving ScatterPlot...") #status
plt.savefig("locations_scatterplot.png")
plt.show()

print("Creating BarPlot...") #status
fig, ax = plt.subplots()
ax.bar(locations.keys(), locations.values())
plt.xticks(rotation=90)
plt.xlabel("Location")
plt.ylabel("Number of Tweets")
plt.title("Locations of Tweets on #flutter")
plt.tight_layout()
print("Saving BarPlot...") #status
plt.savefig("locations_barplot.png")
plt.show()
print("Finished.")