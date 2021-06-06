def fetch_twitter(search_keyword, start_date="2021-5-1", tweet_items=150):

    #import packages for beyonce twitter nlp
    import os
    import tweepy as tw
    import pandas as pd

    #get the twitter token keys

    consumer_key= '56xWSXwoOBV7msHyVYvOuGIL6'
    consumer_secret= 'bfw8JTTl4s1u1Eb0nytY0A5glP99zd253IIySBJ4NOdLrG9227'
    access_token= '1576618256-gGeX97tIFXQO6wH5OMtsZr6LDssDzn9HNyArXwa'
    access_token_secret= '5gzpwJHaE0d1JsBMh0a632xO1k9Te412k5ZWYL0WNi0JG'

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    #Define the search term and the date_since date as variables
    search_words = "#"+search_keyword
    date_since = start_date

# Collect tweets
    tweets = tw.Cursor(api.search,
    q=search_words,
    lang="en",
    since=date_since).items(tweet_items)

    # Iterate and print tweets
    response_string=""
    for tweet in tweets:
        response_string=response_string+" "+tweet.text
    return response_string

