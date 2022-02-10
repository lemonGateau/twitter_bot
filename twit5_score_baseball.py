# coding utf-8
import sys
sys.path.append('..')
import json, config
from requests_oauthlib import OAuth1Session
from line_notify.line_8_score_baseball import today_score
from twit_bot import Twit

def main():
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    AS = config.ACCESS_SECRET

    twit = Twit(CK, CS, AT, AS)

    text = today_score()
    _ = twit.post_tweet(text)


if __name__ == '__main__':
    main()
