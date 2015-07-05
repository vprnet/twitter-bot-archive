#!/usr/bin/python
import json
import requests
import os
import urllib
from datetime import datetime, date
from cStringIO import StringIO
from config import NPR_API_KEY


def api_feed(tag, numResults=1, endDate=2014-07-01):
    """Query the NPR API using given tag ID, return dictionary of results"""

    stories = query_api(tag, numResults)

    story_list = []

    for story in stories:
        link = story['link'][0]['$text']
        date = convert_date(story['storyDate']['$text'])
        title = story['title']['$text'].strip()

        story_list.append({
            'title': title,
            'date': date,
            'link': link
        })

    return story_list


def query_api(tag, numResults=1, endDate=2014-07-01):
    """Hits the NPR API, returns JSON story list"""

    id_string = ','.join([str(s) for s in tag])

    today = date.today()
    last_year = today.replace(year=2014)
    endDate = last_year.isoformat()

    query = ('http://api.npr.org/query?orgid=692' +
        '&fields=title,byline,storyDate,image,text,audio' +
        '&sort=dateDesc' +
        '&action=Or' +
        '&output=JSON' +
        '&numResults=%d' +
        '&id=%s' +
        '&endDate=%s' +
        '&apiKey=%s') % (numResults, id_string, endDate, NPR_API_KEY)

    r = requests.get(query)
    j = json.loads(r.text)
    stories = j['list']['story']

    return stories


def convert_date(timestamp):
    """Converts API timestamp to publication-ready dateline"""

    day = timestamp[5:7]
    month = datetime.strptime(timestamp[8:11], '%b').strftime('%B')
    year = timestamp[12:16]
    date = month + ' ' + day + ", " + year

    return date
