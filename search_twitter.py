#!/usr/bin/python
try:
  import cjson as json
except Exception:
  import json
import urllib2

def get_json(hash_tag):
  try:
    url = 'http://search.twitter.com/search.json?reputable=true&display_location=search-component&pc=true&q={hash_tag}&rpp=100'.format(hash_tag=hash_tag)
    r = urllib2.Request(url, '', { 'User-Agent' : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11" })
    twitter_json = urllib2.urlopen(r,timeout=1).readlines()[0]
    return json.decode(twitter_json)
  except urllib2.HTTPError:
    import time
    time.sleep(10)
    return {'results':{}}

def search_by_hashtags(hash_tag_search):
  # http://api.twitter.com/1/users/search.json?reputable=true&display_location=search-component&pc=true&q=rt+OR+heatmap
  # http://twitter.com/phoenix_search.phoenix?q=rt+heatmap&include_entities=1&include_available_features=1&contributor_details=true&filter=links
  url = 'http://twitter.com/phoenix_search.phoenix?q={hash_tag_search}&include_entities=1&include_available_features=1&contributor_details=true&filter=links'.format(hash_tag_search=hash_tag_search)
  try:
    r = urllib2.Request(url, '', { 'User-Agent' : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11" })
    twitter_json = json.decode(urllib2.urlopen(r,timeout=1).readlines()[0])
    return twitter_json['statuses']
  except urllib2.URLError:
    return {}

