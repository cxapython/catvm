# -*- coding: utf-8 -*-
import os
import re
import json
import hashlib
import requests
import datetime
from scrapy.selector import Selector

from decimal import Decimal

def request_to_json(request):
    req = {}
    req['url'] = request.url
    req['method'] = request.method
    req['body'] = request.body.decode()
    return json.dumps(req)

def parse_json(string):
    '''
    把一个类json字符串转换成json字符串
    '''
    if len(string) == 0:
        raise Exception('argument value {} error'.format(string))

    pattern = r"([a-zA-Z_][a-zA-Z_0-9]*)\s*\:"
    repl = lambda match: '"{}":'.format(match.group(1))
    json_str = string[string.find('{'):string.rfind('}')+1]     # '{' 从前往后找，'}'从后往前找
    json_str = re.sub(pattern, repl, json_str)
    json_str = re.sub(r',+', ',', json_str)  # 把连续的逗号（两个或两个以上）替换成一个逗号
    json_str = re.sub(r',]', ']', json_str)  # 列表中最后一个元素后面不能有逗号，和python语法不同

    return json.loads(json_str)

def parse_date(d):
        if d is None or '-' == d: return None
        else: return datetime.datetime.strptime(d, '%Y-%m-%d').date()

def parse_decimal(d):
        if d is None or '-' in d: return None
        else: return Decimal(d)

def parse_varchar(s):
    if s is None or '-' == s: return None
    else: return s

def checksum(method, file):
    """
    Calculate the checksum of a file-like object without
    reading its whole content in memory.
    """
    m = method()
    while True:
        d = file.read(8096)
        if not d:
            break
        m.update(d)
    return m.hexdigest()

def md5sum(file):
    return checksum(hashlib.md5, file)

def sha1sum(file):
    return checksum(hashlib.sha1, file)

def get_service_url(service_name):
    consul_url = 'http://{}:8500/v1/health/service/{}'.format(os.environ.get('HOST_IP'), service_name)
    resp = requests.get(consul_url, timeout=30)
    nodes = json.loads(resp.text)
    return 'http://{}:{}'.format(nodes[0]['Service']['Address'], nodes[0]['Service']['Port'])

# aws专用：获取notify服务地址
def get_service_url_aws(service_name):
    return 'http://notify.shannonai.com:80'

SPIDERKEEPER_ADDR = 'http://spiderkeeper:5000'
PROJECT_NAME = 'shannon_spider'
def get_log_url(spider_name):
    res = requests.get(SPIDERKEEPER_ADDR + '/api/projects')
    project_id = re.findall(r'\"project_id\": (\d+),\s*?\"project_name\": \"{}\"'.format(PROJECT_NAME), res.text)
    if project_id == []:
        return '项目不存在'
    response = requests.get(SPIDERKEEPER_ADDR + '/api/projects/{}/jobexecs'.format(project_id[0]))
    res_obj = json.loads(response.text)
    run_list = res_obj['RUNNING']
    pendingr_list = res_obj['PENDING']
    job_spider_list = run_list + pendingr_list
    job_id = None
    for job_spider in job_spider_list:
        if spider_name == job_spider['job_instance']['spider_name']:
            job_id = job_spider['job_execution_id']
            break
    if job_id:
        return 'http://sk.shannonai.com/project/{}/jobexecs/{}/log'.format(project_id[0], job_id)
    return 'spider_name没有找到响应id'