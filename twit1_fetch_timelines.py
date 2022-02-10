# coding utf-8
import json, config
from requests_oauthlib import OAuth1Session
from line_notify import line_bot3


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_SECRET
twitter = OAuth1Session(CK, CS, AT, AS)

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

params = {'count': 5}
res = twitter.get(url, params=params)
msg = '\n'

# 正常通信が出来たとき
if res.status_code == 200:
    timelines = json.loads(res.text)
    for line in timelines:
        print(line['user']['name'] + '::' + line['text'])
        print(line['created_at'])
        print('*******************************************')
        msg += line['text'] + '\n' + line['created_at']
else:
    print('Failed: ', res.status_code)

ln.send(message=msg)