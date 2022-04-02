# encoding: utf-8
"""
@author: ZhangPei
@file: translate_util.py
@time: 2018/8/30 14:34

"""
import hashlib
import string

import time

import requests
import json
import logging


class Translate(object):
    ''' 
        百度翻译接口， 具体文档参照
        http://api.fanyi.baidu.com/api/trans/product/apidoc
    '''
    api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    my_appid: str = None  # 百度翻译appid
    cyber: str = None  # 秘钥
    lower_case = list(string.ascii_lowercase)
    from_language: str = None  # 源语言
    to_language: str = None  # 目标语言，一般为中文

    def __init__(self, my_appid, cyber, from_language, to_language):
        self.my_appid = my_appid
        self.cyber = cyber
        self.from_language = from_language
        self.to_language = to_language

    def trans(self, word):
        salt = str(time.time())[:10]
        final_sign = self.my_appid + word + salt + self.cyber
        final_sign = hashlib.md5(final_sign.encode('utf-8')).hexdigest()
        result = None
        param = {
            'q': word,
            'from': self.from_language,
            'to': self.to_language,
            'appid': self.my_appid,
            'salt': salt,
            'sign': final_sign
        }
        try:
            response = requests.get(self.api_url, params=param).content
            content = str(response, encoding="utf-8")
            json_reads = json.loads(content)
            result = json_reads['trans_result'][0]['dst']
            logging.info('翻译完成')
        except Exception:
            logging.error('翻译失败')
        return result
