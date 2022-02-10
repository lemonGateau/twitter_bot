#coding utf-8
import json, config
from requests_oauthlib import OAuth1Session


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_SECRET
twitter = OAuth1Session(CK, CS, AT, AS)

url = 'https://api.twitter.com/1.1/statuses/update.json'

print('tweet内容を入力してください')
tweet = input('>>')

params = {"status": tweet}
res = twitter.post(url, params=params)

# print(res.headers)

if res.status_code == 200:
    tweet = json.loads(res.text)
    print('post tweet.')
    print(tweet['id'])
else:
    print('Failed: ', res.status_code)
