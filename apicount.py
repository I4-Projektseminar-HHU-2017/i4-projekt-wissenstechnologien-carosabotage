# -*- coding: utf-8 -*-

#Python 3

from TwitterSearch import *



try:
    tso = TwitterSearchOrder() 
    tso.set_keywords(['#TWD', 'since:2016-04-03']) # 'since:2017-08-05'   5 Aug 2017
    #tso.set_search_url('q=%23TWD%20since%3A2016-04-03%20until%3A2016-10-23&src=typd')
    tso.set_language('en')
    tso.set_include_entities(False) 
 
    
  

    ts = TwitterSearch(
        consumer_key = 'key',
        consumer_secret = 'secret',
        access_token = 'token',
        access_token_secret = 'tokensecret'
     )
     
    count = 0 


   
    for tweet in ts.search_tweets_iterable(tso):
        count = count + 1   #zählt Anzahl an Tweets     
        print(count, tweet['created_at'], tweet['text'])
 


except TwitterSearchException as e:
    print(e)





# gefunden auf : https://pypi.python.org/pypi/TwitterSearch/



