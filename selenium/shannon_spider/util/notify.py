# -*- coding: utf-8 -*-

import os
import json
import logging
import requests

from shannon_spider.util import get_service_url
from scrapy.utils.project import get_project_settings


# 注意: 必须使用raw string, 不能使用多行字符串, 钉钉只处理没有转义的字符, 包含转义字符会导致解析失败
failure_template = ('### scrapy==》爬虫任务运行中异常报错信息\n\n'
                    '> type: {type}\n\n'
                    '> spider_name: {spider_name}\n\n'
                    '> error_data: {error_data}\n\n'
                    '> log_url: {log_url}\n\n')

def send_dingtalk(type, spider_name, error_data, log_url=""):
    '''
    title: 报警标题
    '''
    if log_url == "":
        return

    try:
        settings = get_project_settings()

        content = failure_template.format(
            type=type,
            spider_name=spider_name,
            error_data=error_data,
            log_url=log_url,
        )

        msg = {
            "msgtype": "markdown",
            "markdown": {
                "title": '爬虫任务进行中报错信息',
                "text": content
            }
        }

        i = 0
        while i < 3:
            i += 1
            resp = requests.post(settings['ROBOT_SPIDER'], json=msg, timeout=30)
            json_data = json.loads(resp.text)
            if resp.status_code == 200 and json_data['errcode'] == 0:
                break
            else:
                logging.error('钉钉报警发送失败{}'.format(json_data['errmsg']))
        
    except Exception as e:
        logging.error("send dingtalk failed, exception: ", e)


failure_template_info = ('### scrapy==》爬虫运行结束后错误信息总结\n\n'
                    '> spider_name: {spider_name}\n\n'
                    '> error_count: {error_count}\n\n'
                    '> log_url: {log_url}\n\n')

def send_dingtalk_info(spider_name, count, log_url):
    '''
    title: 报警标题
    '''
    try:
        settings = get_project_settings()

        content = failure_template_info.format(
            spider_name=spider_name,
            error_count=count,
            log_url=log_url,
            )

        msg = {
            "msgtype": "markdown",
            "markdown": {
                "title": '爬虫任务结束错误信息',
                "text": content
            }
        }

        i = 0
        while i < 3:
            i += 1
            resp = requests.post(settings['ROBOT_SPIDER'], json=msg, timeout=30)
            json_data = json.loads(resp.text)
            if resp.status_code == 200 and json_data['errcode'] == 0:
                break
            else:
                logging.error('钉钉报警发送失败{}'.format(json_data['errmsg']))

    except Exception as e:
        logging.error("send dingtalk failed, exception: ", e)
