# encoding: utf-8
'''
@Author  : 杜艺创
@Time    : 2021/11/26 11:24
@Software: PyCharm
@File    : twitter_people.py
'''
import datetime
import hashlib
import json
import time
import pandas as pd
import requests
from new_db import insert_one, close_mysql, is_exit, update


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


def get_user_id(exec_name, name, gt, country, position, url):
    items = {}
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-guest-token': f'{gt}',
    }

    params = (
        ('variables', f'{{"screen_name":"{name}","withHighlightedLabel":true,"withSuperFollowsUserFields":false}}'),
    )

    response = requests.get('https://twitter.com/i/api/graphql/G07SmTUd0Mx7qy3Az_b52w/UserByScreenNameWithoutResults',
                            headers=headers, params=params)
    data = json.loads(response.text)
    user_id = data.get('data').get('user').get('rest_id')
    name = data.get('data').get('user').get('legacy').get('name')
    screen_name = data.get('data').get('user').get('legacy').get('screen_name')
    followers_count = str(data.get('data').get('user').get('legacy').get('followers_count'))
    friends_count = str(data.get('data').get('user').get('legacy').get('friends_count'))
    description = data.get('data').get('user').get('legacy').get('description')
    location = data.get('data').get('user').get('legacy').get('location')
    profile_image_url_https = data.get('data').get('user').get('legacy').get('profile_image_url_https')
    affiliates_highlighted_label = data.get('data').get('user').get('affiliates_highlighted_label', {})
    if affiliates_highlighted_label:
        official = affiliates_highlighted_label.get('label').get('description')
    else:
        official = ''
    items["exec_name|"] = exec_name
    items["name|"] = name
    items["screen_name|"] = screen_name
    items["followers_count|"] = followers_count
    items["friends_count|"] = friends_count
    items["description|text"] = description
    items["location|"] = location
    items["official|"] = official
    items["country|"] = country
    items["position|"] = position
    items["url|"] = url
    items["profile_image_url_https|text"] = profile_image_url_https
    items["user_id|"] = user_id
    items["sha|"] = set_sha(
        name + screen_name + followers_count + friends_count + description + location + official + profile_image_url_https)
    result = is_exit("twitter_people_info", items["sha|"], items["user_id|"])
    if result == 1:
        update('twitter_people_info', items, items["user_id|"])
    elif result == 2:
        insert_one("twitter_people_info", items, index=["sha"], unique_index=["user_id"])
    else:
        return

def run():
    gt = get_gt()
    urls = read_urls()
    for url in urls:
        exec_name = url[0]
        name_1 = url[1].replace('https://twitter.com/', '').replace('/', '')
        country = url[3]
        position = url[4]
        if type(position) == float:
            position = ''
        try:
            get_user_id(exec_name, name_1, gt, country, position, url[1])
        except:
            print(f'链接: {url[1]}出错')
            pass
        if type(url[2]) != float:
            name_2 = url[2].replace('https://twitter.com/', '').replace('/', '')
            try:
                get_user_id(exec_name, name_2, gt, country, position, url[2])
            except:
                print(f'链接: {url[2]}出错')
                pass
    close_mysql()


if __name__ == '__main__':
    run()
