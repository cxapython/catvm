import re
from lxml import etree
import requests
import execjs


proxyHost = "http-pro.abuyun.com"
proxyPort = "9010"
proxyUser = 'H5686N8652T8UK8P'
proxyPass = '02F2327FEFDD0428'
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

def get_sign(token, max_behot_time):
    if max_behot_time == 0:
        param = '/api/pc/feed/?category=pc_profile_article&utm_source=toutiao&visit_user_token={}&max_behot_time=0'.format(
            token)
    else:
        param = '/api/pc/feed/?category=pc_profile_article&utm_source=toutiao&visit_user_token={}&max_behot_time={}'.format(
            token, max_behot_time)
    sign_url = 'https://www.toutiao.com' + "/toutiao" + param
    js = ''
    with open('sign.js') as r:
        js += r.read()
    js = execjs.compile(js)
    sign = "&_signature=" + js.call('get_sign', sign_url, '').replace('\n', '')
    return sign


def get_cookie():
    js = ''
    with open('sign.js') as r:
        js += r.read()
    js = execjs.compile(js)
    cookies = js.call('get_cookie')

    return cookies


urls = [
    'https://www.toutiao.com/c/user/token/MS4wLjABAAAAWg_9yQwMz4S3FCVaBPvCYI2OK1lg3kLnMx6ijEJaTP0/',

    'https://www.toutiao.com/c/user/token/MS4wLjABAAAAl-X3cVvO_WPC4EyprOsw6kwD3zaQU29cdI7lPlYBxxA/',

    'https://www.toutiao.com/c/user/token/MS4wLjABAAAA5OOU8SqIiUYQGySWidV1WjpBTJb7z2UXwLy_G5RdExA/',
]
for url in urls:
    token = re.search('token/(\S*?)/', url).group(1)
    url = 'https://www.toutiao.com/api/pc/feed/?category=pc_profile_article&utm_source=toutiao&visit_user_token={}&max_behot_time=0'.format(
        token)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }

    sign = get_sign(token, max_behot_time=0)
    req_url = url + sign
    response = requests.get(url=req_url, headers=headers)
    json_data = response.json()
    for k in json_data.get('data'):
        k_dic = {}
        k_dic['title'] = k.get('title')
        print(k_dic)
        url = f'https://www.toutiao.com/a{k.get("group_id")}/'
        cookies = get_cookie()
        __ac_nonce = dict(cookies).get('__ac_nonce')
        __ac_signature = dict(cookies).get('__ac_signature')
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77',
            'cookie': f'ttwid=1%7CONMkZLzM-l5vqAPMB7wSQnQ5kS9ApwVc5vkCRj3BlTI%7C1618810910%7Cbe794d2633fbec045d4403bd2933c4badda3d904b5c67dc1813ba57f1d933f0f; __ac_nonce={__ac_nonce}; __ac_signature={__ac_signature};'
        }
        resp = requests.get(url=url, headers=headers, proxies=proxies)
        html = etree.HTML(resp.text)
        try:

            title = html.xpath('''//div[@class='article-content']/h1/text()''')[0]
            print(title)
        except:
            print(resp.status_code)
            print(resp.text)
            pass
    print('---------------------第一页-----------------')
    max_behot_time = json_data.get('next').get('max_behot_time')
    next_url = f'https://www.toutiao.com/api/pc/feed/?category=pc_profile_article&utm_source=toutiao&visit_user_token={token}&max_behot_time={max_behot_time}'
    next_req_url = next_url + get_sign(token, max_behot_time=max_behot_time)
    response = requests.get(url=next_req_url, headers=headers , proxies=proxies)
    json_data = response.json()
    for k in json_data.get('data'):
        k_dic = {}
        k_dic['title'] = k.get('title')
        # k_dic['group_id'] = k.get('group_id')
        url = f'https://www.toutiao.com/a{k.get("group_id")}/'
        cookies = get_cookie()
        __ac_nonce = dict(cookies).get('__ac_nonce')
        __ac_signature = dict(cookies).get('__ac_signature')
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77',
            'cookie': f'ttwid=1%7CONMkZLzM-l5vqAPMB7wSQnQ5kS9ApwVc5vkCRj3BlTI%7C1618810910%7Cbe794d2633fbec045d4403bd2933c4badda3d904b5c67dc1813ba57f1d933f0f; __ac_nonce={__ac_nonce}; __ac_signature={__ac_signature};'
        }
        resp = requests.get(url=url, headers=headers)
        html = etree.HTML(resp.text)
        try:
            title = html.xpath('''//div[@class='article-content']/h1/text()''')[0]
            print(title)
        except:
            print(resp.status_code)
            print(resp.text)
            pass
# ttcid=b597107ff00645cf83f74d60bd0c688123; tt_webid=6945703380611581470; _tea_utm_cache_2256={%22utm_source%22:%22weixin%22%2C%22utm_medium%22:%22toutiao_android%22%2C%22utm_campaign%22:%22client_share%22}; csrftoken=a3697f4f7c5c8778bca02bdd7870c310; ttwid=1%7CONMkZLzM-l5vqAPMB7wSQnQ5kS9ApwVc5vkCRj3BlTI%7C1618810910%7Cbe794d2633fbec045d4403bd2933c4badda3d904b5c67dc1813ba57f1d933f0f; tt_webid=6952739902379640350; __ac_nonce=0607e32a700e4f2edea3; s_v_web_id=verify_knpda967_LGymDgky_hg6u_4EmV_A6a2_zNgqGYovEIQC; __ac_signature=_02B4Z6wo00f01Okb.xAAAIDDWeoT2ooBJJDpP.uAAFo-NonJqFyTKwz8PBKnEsOLvs2xzOD-s.PyGxNcEk3dTAMF8OAqLV-EhjcAdkQ7AX0KIlyjoaTd8S-r9e-5V0HkRNrl4kulNVY4duGt87; MONITOR_WEB_ID=e4d12f66-9959-46b5-9a50-ed52f6d2542e; tt_scid=UOPDYyyEgzozZkciZbGfmL.m1BJDFhj93hSbRe4vviyHQcsvGrwVYWcoEu4wHZBG0a88
# ttcid=b597107ff00645cf83f74d60bd0c688123; tt_webid=6945703380611581470; _tea_utm_cache_2256={%22utm_source%22:%22weixin%22%2C%22utm_medium%22:%22toutiao_android%22%2C%22utm_campaign%22:%22client_share%22}; csrftoken=a3697f4f7c5c8778bca02bdd7870c310; ttwid=1%7CONMkZLzM-l5vqAPMB7wSQnQ5kS9ApwVc5vkCRj3BlTI%7C1618810910%7Cbe794d2633fbec045d4403bd2933c4badda3d904b5c67dc1813ba57f1d933f0f; tt_webid=6952739902379640350; __ac_nonce=0607e32a700e4f2edea3; s_v_web_id=verify_knpda967_LGymDgky_hg6u_4EmV_A6a2_zNgqGYovEIQC; __ac_signature=_02B4Z6wo00f01Okb.xAAAIDDWeoT2ooBJJDpP.uAAFo-NonJqFyTKwz8PBKnEsOLvs2xzOD-s.PyGxNcEk3dTAMF8OAqLV-EhjcAdkQ7AX0KIlyjoaTd8S-r9e-5V0HkRNrl4kulNVY4duGt87; MONITOR_WEB_ID=e4d12f66-9959-46b5-9a50-ed52f6d2542e; tt_scid=xW3CFgKS9i4lOaGO8K-DFO1Ejn5WTYuodv0pRTLq-uzw1ne5g.qGzgqlYz1NpiIhe6b7
# ttcid=b597107ff00645cf83f74d60bd0c688123; tt_webid=6945703380611581470; _tea_utm_cache_2256={%22utm_source%22:%22weixin%22%2C%22utm_medium%22:%22toutiao_android%22%2C%22utm_campaign%22:%22client_share%22}; csrftoken=a3697f4f7c5c8778bca02bdd7870c310; ttwid=1%7CONMkZLzM-l5vqAPMB7wSQnQ5kS9ApwVc5vkCRj3BlTI%7C1618810910%7Cbe794d2633fbec045d4403bd2933c4badda3d904b5c67dc1813ba57f1d933f0f; tt_webid=6952739902379640350; __ac_nonce=0607e32a700e4f2edea3; s_v_web_id=verify_knpda967_LGymDgky_hg6u_4EmV_A6a2_zNgqGYovEIQC; __ac_signature=_02B4Z6wo00f01Okb.xAAAIDDWeoT2ooBJJDpP.uAAFo-NonJqFyTKwz8PBKnEsOLvs2xzOD-s.PyGxNcEk3dTAMF8OAqLV-EhjcAdkQ7AX0KIlyjoaTd8S-r9e-5V0HkRNrl4kulNVY4duGt87; MONITOR_WEB_ID=e4d12f66-9959-46b5-9a50-ed52f6d2542e; tt_scid=uZs-2sJj0xGKtcmHB3rwWcYx2h.E8Ars3FfTKyYBQA35Nd54WY3bgkI-3T--pS5B49e3