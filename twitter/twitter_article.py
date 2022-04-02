# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/11/26 15:17
@Software: PyCharm
@File    : twitter_article.py
'''
import datetime
import hashlib
import json
import time
import pandas as pd
import requests

from new_db import is_exit, insert_one, close_mysql, update


def read_urls():
    urls = []
    excel = pd.read_excel('people.xlsx', sheet_name=0, usecols=[0, 1, 2, 3, 4])
    urls_ = excel.values.tolist()
    for url in urls_:
        urls.append(url)
    return urls


def set_sha(data):
    hash_code = hashlib.sha1()
    hash_string = ''
    for value in data:
        hash_string += str(value)
    hash_code.update(hash_string.encode('utf-8'))
    sha = hash_code.hexdigest()
    return sha


def get_gt():
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    }
    response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers)
    data = json.loads(response.text)
    gt = data.get('guest_token')
    return gt


def get_user_id(name, gt):
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-guest-token': f'{gt}',
    }

    params = (
        ('variables', f'{{"screen_name":"{name}","withHighlightedLabel":true,"withSuperFollowsUserFields":false}}'),
    )

    response = requests.get('https://twitter.com/i/api/graphql/G07SmTUd0Mx7qy3Az_b52w/UserByScreenNameWithoutResults',
                            headers=headers, params=params)
    user_id = json.loads(response.text).get('data').get('user').get('rest_id')
    return user_id


def crawl(name):
    gt = get_gt()
    user_id = get_user_id(name, gt)
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-guest-token': f'{gt}',
    }

    params = (
        ('variables',
         '{"userId":"%s","count":1000,"withHighlightedLabel":false,"withTweetQuoteCount":false,"includePromotedContent":false,"withTweetResult":true,"withReactions":false,"withSuperFollowsTweetFields":false,"withSuperFollowsUserFields":false,"withUserResults":false,"withClientEventToken":false,"withBirdwatchNotes":false,"withBirdwatchPivots":false,"withVoice":true}' % user_id),
    )

    response = requests.get('https://twitter.com/i/api/graphql/SvuhrsBPMT3klXIONc0gtQ/UserTweets', headers=headers,
                            params=params)
    return response.json()


def parse(exec_name, data, url):
    items = {}
    data_list = data.get('data').get('user').get('result').get('timeline').get('timeline').get('instructions')[1].get(
        'entries')
    for data_dict in data_list:
        entry_id = data_dict.get('entryId')
        try:
            retweeted_status_result = data_dict.get('content').get('itemContent').get('tweet_results').get(
                'result').get('legacy').get('retweeted_status_result', {})
        except:
            continue
        if retweeted_status_result:
            full_text = retweeted_status_result.get('result').get('legacy').get('full_text')
            favorite_count = retweeted_status_result.get('result').get('legacy').get('favorite_count')
            reply_count = retweeted_status_result.get('result').get('legacy').get('reply_count')
            retweet_count = retweeted_status_result.get('result').get('legacy').get('retweet_count')
            created_at = retweeted_status_result.get('result').get('legacy').get('created_at')
            retweet_name = retweeted_status_result.get('result').get('core').get('user').get('legacy').get('name')
            retweet_screen_name = retweeted_status_result.get('result').get('core').get('user').get('legacy').get(
                'screen_name')
            created_at = datetime.datetime.strftime(
                datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y'),
                '%Y-%m-%d %H:%M:%S')
            crawl_time = int(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d'))
        else:
            full_text = data_dict.get('content').get('itemContent').get('tweet_results').get('result').get(
                'legacy').get('full_text')
            favorite_count = data_dict.get('content').get('itemContent').get('tweet_results').get('result').get(
                'legacy').get('favorite_count')
            reply_count = data_dict.get('content').get('itemContent').get('tweet_results').get('result').get(
                'legacy').get('reply_count')
            retweet_count = data_dict.get('content').get('itemContent').get('tweet_results').get('result').get(
                'legacy').get('retweet_count')
            created_at = data_dict.get('content').get('itemContent').get('tweet_results').get('result').get(
                'legacy').get('created_at')
            created_at = datetime.datetime.strftime(
                datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y'),
                '%Y-%m-%d %H:%M:%S')
            crawl_time = int(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d'))
            retweet_name = ''
            retweet_screen_name = ''
        ctime = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        c_time = datetime.datetime.now() - datetime.timedelta(days=365)
        if ctime < c_time:
            continue
        items["exec_name|"] = exec_name
        items["entry_id|"] = entry_id
        items["full_text|text"] = full_text
        items["favorite_count|"] = favorite_count
        items["reply_count|"] = reply_count
        items["retweet_count|"] = retweet_count
        items["retweet_name|"] = retweet_name
        items["retweet_screen_name|"] = retweet_screen_name
        items["url|"] = url
        items["created_at|"] = created_at
        items["crawl_time|"] = crawl_time
        items["sha|"] = set_sha(str(favorite_count) + str(reply_count) + str(retweet_count))
        result = is_exit("twitter_article", items["sha|"], items["entry_id|"], unique='entry_id')
        if result == 1:
            update_items = {}
            update_items["favorite_count|"] = favorite_count
            update_items["reply_count|"] = reply_count
            update_items["retweet_count|"] = retweet_count
            update('twitter_article', update_items, items["entry_id|"], unique='entry_id')
        elif result == 2:
            insert_one("twitter_article", items, index=["sha"], unique_index=["entry_id"])
        else:
            continue


def run():
    urls = read_urls()
    for url in urls:
        time.sleep(3)
        exec_name = url[0]
        name_1 = url[1].replace('https://twitter.com/', '').replace('/', '')
        try:
            data = crawl(name_1)
            parse(exec_name, data, url[1])
        except:
            print(f'出错了: {url[1]}')
            pass
        if type(url[2]) != float:
            name_2 = url[2].replace('https://twitter.com/', '').replace('/', '')
            try:
                data = crawl(name_2)
                parse(exec_name, data, url[2])
            except:
                print(f'出错了: {url[2]}')
                pass


if __name__ == '__main__':
    run()
