# coding=utf-8
import requests

def send_dingtalk_info(robot_url, content, notify_url):
    '''
    title: 信息标题
    '''
    msg = {}
    msg['robot'] = robot_url
    msg['title'] = 'tushare数据监控'
    msg['content'] = content
    resp = requests.post(notify_url, json=msg, timeout=30)

def failure_to_exc_info(failure):
    """Extract exc_info from Failure instances"""
    return (failure.type, failure.value, failure.getTracebackObject())