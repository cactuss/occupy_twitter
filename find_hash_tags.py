#!/usr/bin/python
"""
What we're going to do here is find all co-occuring tags with #ows and #occupywallstreet

"""
import search_twitter
import hashtag_regex
core_hash_tags = ['%23ows', '%23occupywallstreet']

found_hash_tags = {} # key is hashtag value is count

for hash_tag in core_hash_tags:
  twitter_data = search_twitter.get_json(hash_tag)
  for tweet in twitter_data['results']:
    #print tweet['text']
    hash_tags = hashtag_regex.get_hashtags_from_string(tweet['text'].lower())
    for match in hash_tags:
      if match.find('occupy') == -1:
        continue
      if not found_hash_tags.has_key(match):
        found_hash_tags[match] = 0
      found_hash_tags[match] +=1
        
      
for key in found_hash_tags.iterkeys():
  print key,found_hash_tags[key]
