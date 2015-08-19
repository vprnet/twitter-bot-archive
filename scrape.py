import requests
import random
from datetime import date
from BeautifulSoup import BeautifulSoup

def new_archive_tweet():
    slug = random.randint(74271, 98141)
    random_story = str(slug)

    url = 'http://www.vpr.net/news_detail/' + random_story
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)

    headline = soup.find('h2')
    story_date = soup.find('h4')

    random_archive_headline = headline.text
    random_archive_date = story_date.text[:8]

    tweet = random_archive_date + ": " + random_archive_headline + " " + url

    return tweet
