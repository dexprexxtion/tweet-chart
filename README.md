# tweet-chart 🐦📊
## v1.0.0 🚀
Fetch Tweets from Twitter and display them in a chart. Can be used for research purposes.
>The code is ready for usage but is under development to add more features. 🚀

## How to use
---
- Get your Twitter Developer Account API keys from https://developer.twitter.com/en/portal/dashboard.
- Put them in the `.env.template` file.
- Rename the file from `.env.template` to `.env`.
- Now open `main.py` and modify the `hashtag` and `number_of_tweets` variables on Line 9 and 10 to your desired values.
- Now run `main.py` in the terminal using python.

## Features To-Do ☑️
[ ] Add visual UI

[ ] Optimize code perfomance

[ ] Make a website to use this tool on the web

## How it works 🤔
### Code explanation 

The `main.py` file first imports the `tweepy`, `os`, `geopy`, `matplotlib.pyplot` as `plt`, `load_dotenv` from `dotenv` and `Nominatim` from `geopy.geocoders`.

Then variables containing information about the `version`, `number_of_tweets` to be fetched and the `hashtag` of which the tweets have to be fetched.

The `load_dotenv()` function is then used to load the environment variables containing the API keys, secrets and access token credentials.

The program displays the version and the status.

Now, the below code

`auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))`

retrieves the credentials and sets the access token with `tweepy.OAuthHandler`.

Then, `api = tweepy.API(auth)` authenticates with OAuth Twitter API.

The program then search for tweets with the hashtag provided with `tweepy.Cursor().items(number_of_tweets)`.

A locations dictionary is then created with `locations = {}` to store the locations of the user's tweets.

`geolocator Nominatim` is used to obtain the latitudes and longitudes of the users' tweets.

`plt.scatter` is then used to create a ScatterPlot and then a BarPlot is made. The charts are then displayed and saved after closing the dialog.

