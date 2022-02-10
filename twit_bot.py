#coding utf-8
import json, config
import urllib.parse
from requests_oauthlib import OAuth1Session


class Twit:
    def __init__(self, CK, CS, AT, AS):
        self.twit = OAuth1Session(CK, CS, AT, AS)
        self.end_point = 'https://api.twitter.com/'

    def __get_requests(self, path, query_str=None):
        if query_str is None:
            url = self.end_point + path
        else:
            url = self.end_point + path + '?' + query_str

        return self.twit.get(url)

    def __post_requests(self, path, params=None):
        ''' v1.1 '''
        url = self.end_point + path

        if params is None:
            return self.twit.post(url)

        return self.twit.post(url, params=params)

    def fetch_tweet_info(self, tweet_id):
        ''' ToDo: query_paramsの指定 '''
        path = f'2/tweets/{tweet_id}'

        return self.__get_requests(path)

    def fetch_user_timelines(self, user_id, max_results=10):
        path = f'2/users/{user_id}/tweets'

        params = {"max_results": max_results}
        query_str = urllib.parse.urlencode(params)

        return self.__get_requests(path, query_str)

    def post_tweet(self, text):
        ''' v1,1 '''
        path = '1.1/statuses/update.json'
        params = {"status": text}

        return self.__post_requests(path, params=params)

    def delete_tweet(self, tweet_id):
        ''' v1.1 '''
        path = f'1.1/statuses/destroy/{tweet_id}.json'
        params = {"id": tweet_id}

        return self.__post_requests(path, params=params)

    def fetch_user_mentions(self, user_id, max_results=10):
        ''' 指定ユーザに関連する(@user_nameを含む)ツイートを取得 '''
        path = f'2/users/{user_id}/mentions'

        params = {"max_results": max_results}
        query_str = urllib.parse.urlencode(params)

        return self.__get_requests(path, query_str)

    def search_tweets(self, search_word, max_results=10):
        ''' 直近7日間のツイートから検索 '''
        path = '2/tweets/search/recent'

        params = {"query": search_word, "max_results": max_results}
        query_str = urllib.parse.urlencode(params)

        return self.__get_requests(path, query_str)


def main():
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    AS = config.ACCESS_SECRET
    twit = Twit(CK, CS, AT, AS)

    USER_ID = config.USER_ID
    tweet_id = '1384083107066744832'
    search_word = 'oreilly japan'

    # res = twit.post_tweet(text='rakuten hand')
    res = twit.delete_tweet(tweet_id)

    # 正常通信が出来たとき
    if res.status_code == 200:
        timelines = json.loads(res.text)
        print(json.dumps(timelines, indent=4))

        for timeline in timelines['data']:
            print(timeline['text'])
            print('*******************************************')
    else:
        print('Failed: ', res.status_code)


if __name__ == '__main__':
    main()
