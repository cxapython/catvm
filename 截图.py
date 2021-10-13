import datetime
from lxml import etree
from selenium import webdriver
import pymysql
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import ImageGrab
import os
from apscheduler.schedulers.blocking import BlockingScheduler

urls = [
    {'title': '''//ul[@id='news_list']/li[@class='pangulist']/div[@class='right']/a/h3/text()''',
     'seed_url': 'http://www.jwview.com/pg.html', 'site': 'jwview', 'encode': 'gb2312'},
]


def run(cursor, browser, conn, path):
    for url in urls:
        browser.get(url.get('seed_url'))
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//title')))
        html = browser.page_source
        html = etree.HTML(html)
        titles = html.xpath('''{}'''.format(url.get('title')))
        save(titles, url.get('site'), cursor, conn, path)


def save(titles, site, cursor, conn, path):
    date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M')
    for title in titles:
        try:
            sql = "insert into test (title,date) value (%s,%s)"
            cursor.execute(sql, (title.replace('"','').strip(), date))
            conn.commit()
        except:
            continue

    width = 1920
    height = 1080
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img.save('{}/{}.jpg'.format(path, site))


def job():
    browser = webdriver.Chrome()
    browser.maximize_window()
    date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S')
    path = '{}'.format(date)
    os.mkdir(path)
    conn = pymysql.connect(host="xx.xx.xx.xx", user="root", password="123456", port=3333, database="internal_dp",
                           charset="utf8")
    cursor = conn.cursor()
    run(cursor, browser, conn, path)
    conn.close()
    browser.close()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', minute=f"*/{5}")
    scheduler.start()
