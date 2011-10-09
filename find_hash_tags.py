#!/usr/bin/python
"""
What we're going to do here is find all co-occuring tags with #ows and #occupywallstreet

"""
import search_twitter

core_hash_tags = ['%23ows', '%23occupywallstreet']

for hash_tag in core_hash_tags:
  twitter_data = search_twitter.get_json(hash_tag)
  for tweet in twitter_data['results']:
    print tweet['text']
    #todo regex using "/\#([a-zA-Z0-9\.\-\_]*)/" all of the hashtags in the post and add to some sort of persistent data store (sql or leveldb/keyval?)
