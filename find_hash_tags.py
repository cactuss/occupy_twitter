#!/usr/bin/python
"""
What we're going to do here is find all co-occuring tags with #ows and #occupywallstreet

"""
import search_twitter
import hashtag_regex
import mysql_shit

core_hash_tags = ['%23ows', '%23occupywallstreet','%23occupywallst']

found_hash_tags = {} # key is hashtag value is count

global_dict = {}
global_dict['max_id'] = {}
global_dict['cnt'] = 0

def get_max_id(hash_tag):
  max_id = 0
  if global_dict['max_id'].has_key(hash_tag):
    max_id = global_dict['max_id'][hash_tag];
  return max_id

def run():
  for hash_tag in core_hash_tags:
    twitter_data = search_twitter.get_json(hash_tag)
    max_id = get_max_id(hash_tag)
    for tweet in twitter_data['results']:
      if tweet['id'] > max_id:
        hash_tags = hashtag_regex.get_hashtags_from_string(tweet['text'].lower())
        for match in hash_tags:
          if match.startswith('occupy') == False:
            continue
          if not found_hash_tags.has_key(match):
            found_hash_tags[match] = 0
          found_hash_tags[match] +=1
          global_dict['cnt'] +=1
    global_dict['max_id'][hash_tag] = twitter_data['max_id']

 
  for key in found_hash_tags.iterkeys():
    mysql_shit.update_hash_tag(key,found_hash_tags[key])

if __name__ == '__main__':
  import time
  cnt = 0
  while True:
    run()
    cnt+=1
    print 'ran',cnt, 'times'
    print 'found',global_dict['cnt'], 'hash tags'
    time.sleep(1)
