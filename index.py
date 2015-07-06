from config import NPR_API_KEY
from query import api_feed
from datetime import date

def new_tweet():
    tags = [178480359]
    story = api_feed(tags, numResults=1)
    today = date.today()

    if date.weekday(today) == 3:
        return (story)[0]['date'] + ": " + (story)[0]['title'] + " " + (story)[0]['link'] + " #tbt"
    else:
        return (story)[0]['date'] + ": " + (story)[0]['title'] + " " + (story)[0]['link']
