#!/usr/bin/python
"""
What we're going to do here is search twitter for all tweets contained in the hash_tags table
and insert them into the tweets table.
"""

import mysql_shit
import pprint
import search_twitter
import os

def get_urls_from_status(status):
  urls = {}
  urls_twitter = status['entities']['urls']
  for url in urls_twitter:
    tmp_url = url['expanded_url']
    if tmp_url == None:
      tmp_url = url['url']
    escaped_tmp_url = tmp_url.replace('\\','')
    urls[ escaped_tmp_url ] = 0
    return urls.keys()

def get_hashtags_from_status(status):
  hashtags = {}
  hashtags_twitter = status['entities']['hashtags']
  for tmp_hashtag in hashtags_twitter:
    tmp_hashtag = tmp_hashtag['text'].lower()
    if tmp_hashtag.startswith('occupy') or tmp_hashtag == 'ows':
      hashtags[tmp_hashtag] = 0
  return hashtags.keys()

""" return orm esque map from what twitter's api asks for to what goes into sql"""
def get_status_sql_dict(status):
  urls_twitter = status['entities']['urls']
  get_dict = {}
  get_dict['hashtags'] = get_hashtags_from_status(status)
  get_dict['urls'] = get_urls_from_status(status)
  get_dict['data'] = status
  return get_dict
import cjson as json
def emit_dict(sql_status_dict):
  if sql_status_dict['hashtags'] and sql_status_dict['urls']:
    for hashtag in sql_status_dict['hashtags']:
      for url in sql_status_dict['urls']:
        ows_write(hashtag+"\t"+url+"\t"+json.encode(sql_status_dict))

def ows_write(line):
  check_rotate_log()
  log_fp.write(line.encode("UTF8")+'\n')


def check_rotate_log():
  global log_fp, log_time
  if time.time() - log_time > 3600/2:#half hour
    log_fp.close()
    os.system('nohup gzip log/'+str(log_time)+'.json &' )

    log_time = time.time()
    log_fp = open('log/'+str(log_time)+'.json','w')
    
import time
log_time = time.time()
log_fp = open('log/'+str(log_time)+'.json','w')


while True:
  hash_tags = mysql_shit.get_all_hash_tags()

  searches = []
  cnt = -1
  flag = True
  while flag:
    cnt+=1
    searches.append([])
    for i in range(20):
      try:
        searches[cnt].append('%23'+hash_tags.pop())
      except IndexError:
        flag = False
    searches[cnt] = '%20OR%20'.join(searches[cnt])


  for search in searches:
    statuses = search_twitter.search_by_hashtags(search)
    for status in statuses:
      sql_status_dict = get_status_sql_dict(status)
      emit_dict(sql_status_dict)
