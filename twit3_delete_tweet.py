#coding utf-8
import json, config
from requests_oauthlib import OAuth1Session


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_SECRET
twitter = OAuth1Session(CK, CS, AT, AS)

tweet_id = 1383251853576605698

url = f'https://api.twitter.com/1.1/statuses/destroy/{tweet_id}.json'

params = {"id": tweet_id}
res = twitter.post(url, params=params)

if res.status_code == 200:
    print('delete tweet.')
else:
    print('Failed: ', res.status_code)
