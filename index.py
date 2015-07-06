from config import NPR_API_KEY
from query import api_feed
from datetime import date
import random

def new_tweet():
    tags = [178480359]
    story = api_feed(tags, numResults=5)
    random_story = (random.choice(story))
    today = date.today()

    if date.weekday(today) == 3:
        return (random_story)['date'] + ": " + (random_story)['title'] + " " + (random_story)['link'] + " #tbt"
    else:
        return (random_story)['date'] + ": " + (random_story)['title'] + " " + (random_story)['link']
