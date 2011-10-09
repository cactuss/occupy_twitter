#!/usr/bin/python
try:
  import cjson as json
except Exception:
  import json
import urllib2

def get_json(hash_tag):
  url = 'http://search.twitter.com/search.json?reputable=true&display_location=search-component&pc=true&q={hash_tag}&rpp=100'.format(hash_tag=hash_tag)
  r = urllib2.Request(url, '', { 'User-Agent' : "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11" })
  twitter_json = urllib2.urlopen(r).readlines()[0]
  return json.decode(twitter_json)
