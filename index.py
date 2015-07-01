from config import NPR_API_KEY
from query import api_feed
import random

def new_tweet():
    tags = [178480359]
    story = api_feed(tags, numResults=5, endDate=2014-07-01)
    random_story = (random.choice(story))
    return (random_story)['date'] + ": " + (random_story)['title'] + " " + (random_story)['link']
