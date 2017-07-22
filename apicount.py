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
        consumer_key = 'n437aK3zV2o2LmDejfVJOdOrU',
        consumer_secret = '8mt2ysZeR2BuyDS8QE5CfcaD6Of4sdUxvSFKVpENcVtC68kzjk',
        access_token = '1445658510-RGZHmLmtkH5BjIPeV6SqN3sDahzBfy3Oj1rNVL5',
        access_token_secret = 'bQ9gaj39xgIdmkZ0AuKOGNZIRBnAtanAZftpo9ls2p21v'
     )
     
    count = 0 


   
    for tweet in ts.search_tweets_iterable(tso):
        count = count + 1   #zählt Anzahl an Tweets     
        print(count, tweet['created_at'], tweet['text'])
 


except TwitterSearchException as e:
    print(e)





# gefunden auf : https://pypi.python.org/pypi/TwitterSearch/



