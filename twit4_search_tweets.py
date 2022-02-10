#coding utf-8
import json, config
import urllib.parse
from requests_oauthlib import OAuth1Session


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_SECRET
twitter = OAuth1Session(CK, CS, AT, AS)

keyword = 'c++'

params = {"q": keyword, "lang": "ja", "count": 10}
query_str = urllib.parse.urlencode(params)

url = f'https://api.twitter.com/1.1/search/tweets.json?{query_str}'

res = twitter.get(url, params=params)

if res.status_code == 200:
    tweets = json.loads(res.text)
    print(json.dumps(tweets, indent=4))
    for tweet in tweets['statuses']:
        print(tweet['created_at'])
        print(tweet['text'])
        print('*******************************************')
else:
    print('Failed: ', res.status_code)
