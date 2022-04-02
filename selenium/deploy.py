# -*- encoding: utf-8 -*-

import os
cur_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
import re
import sys
import fnmatch
import git
import json
import requests
import shutil
import argparse
import subprocess
from string import Template


def find_files(pattern, path):
    '''
    查找满足pattern的文件
    '''
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
        for name in dirs:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def get_commit_id():
    # check if git repository is clean
    repo = git.Repo(cur_dir)
    if repo.is_dirty():
        print('git repository is dirty, please commit first.')
        sys.exit(1)
    commit_id = repo.head.commit.hexsha[:10]
    return commit_id

def prepare_setup(d):
    # template inflate
    with open(os.path.join(cur_dir, 'setup-template.py'), 'rt') as fin:
        src = Template(fin.read())
        result = src.substitute(d)
        with open(os.path.join(cur_dir, 'setup.py'), 'wt') as fout:
            fout.write(result)

def build_egg():
    # build egg
    shutil.rmtree(os.path.join(cur_dir, 'dist'), ignore_errors=True)
    cmd = 'cd {}; python setup.py bdist_egg'
    cmd = cmd.format(cur_dir)
    result = subprocess.run(cmd, shell=True, executable='/bin/bash')
    if result.returncode != 0:
        raise Exception('build egg error, return code:{}'.format(result.returncode))

def deploy_egg(host, port, project_name):
    # deploy egg
    egg_files = find_files('*.egg', os.path.join(cur_dir, 'dist'))
    if len(egg_files) > 1:
        raise Exception('ERROR: there are more than one egg files')
    elif len(egg_files) == 0:
        raise Exception('ERROR: egg file not found')

    # deploy to spiderkeeper
    session = requests.session()
    base_url = 'http://{host}:{port}'.format(host=host, port=port)
    resp = session.get(os.path.join(base_url, 'project/manage'))
    if not resp.ok:
        raise Exception('visit {} failed'.format(base_url))
    resp = session.get(os.path.join(base_url, 'api/projects'))
    projects = json.loads(resp.text)
    project_id = None
    for project in projects:
        if project['project_name'] == project_name:
            project_id = project['project_id']
            break
    if project_id is None:
        raise Exception('ERROR: project {} not found'.format(project_name))

    files = {'file': (open(egg_files[0], 'rb'))}
    headers = {}
    headers['Origin'] = base_url
    headers['Referer'] = os.path.join(base_url, 'project/{}/spider/deploy'.format(project_id))
    upload_url = os.path.join(base_url, 'project/{}/spider/upload'.format(project_id))
    resp = session.post(upload_url, files=files, stream=True, allow_redirects=True, headers=headers)
    if not resp.ok:
        raise Exception('ERROR: deploy failed. status code: {}, reason: {}\n'.format(resp.status_code, resp.reason))

def clean():
    # 删除中间文件
    try:
        shutil.rmtree(os.path.join(cur_dir, 'build'), ignore_errors=True)
        egg_infos = find_files('*.egg-info', cur_dir)
        for egg_info in egg_infos:
            shutil.rmtree(egg_info, ignore_errors=True)
        os.remove(os.path.join(cur_dir, 'setup.py'))
    except Exception as e:
        pass

def get_services(service_name):
    if 'HOST_IP' not in os.environ:
        raise Exception('environment HOST_IP not found, which should be consul listened ip')
    if not args.dns:
        consul_url = 'http://{}:8500/v1/health/service/{}'.format(os.environ.get('HOST_IP'), service_name)
        resp = requests.get(consul_url, timeout=30)
        nodes = json.loads(resp.text)
        if len(nodes) == 0:
            raise Exception('service {} not found'.format(service_name))
        services = []
        for node in nodes:
            services.append((node['Service']['Address'], node['Service']['Port']))
        return services
    services = [(os.environ.get('HOST_IP'), '5000')]
    return services

def main():
    commit_id = get_commit_id()
    d= {}
    d['version'] = commit_id
    prepare_setup(d)
    build_egg()
    spiderkeeper_services = get_services('spiderkeeper')
    deploy_egg(spiderkeeper_services[0][0], spiderkeeper_services[0][1], 'shannon_spider')
    clean()

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    # use DNS(Add Parameter -dns)
    parse.add_argument('-dns', action='store_true')
    args = parse.parse_args()
    sys.exit(main())
