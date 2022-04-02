# -*- coding: utf-8 -*-

# Scrapy settings for shannon_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import os


BOT_NAME = 'shannon_spider'
SPIDER_MODULES = ['shannon_spider.spiders']
NEWSPIDER_MODULE = 'shannon_spider.spiders'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# DB config
CRAWLED_DATABASE = 'mysql+pymysql://{{ DB_USER }}:{{ DB_PASSWORD }}@{{ DB_HOST }}/{{ DB_NAME }}?charset=utf8'
ORIGIN_DATABASE = 'mysql+pymysql://{{ DB_USER }}:{{ DB_PASSWORD }}@{{ DB_HOST }}/{{ DB_NAME }}?charset=utf8'
ECHO_SQL = False

# Logging settings
LOG_STDOUT = False
LOG_LEVEL = 'INFO'
#LOG_FILE = 'shannon_spider.log'
LOG_FORMAT = '%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1
CONCURRENT_REQUESTS = 16
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True

COOKIES_ENABLED = True
COOKIES_DEBUG = True

#SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
#SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# default user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
   'Cache-Control': 'no-cache',
   'Connection': 'keep-alive',
   'DNT': '1',
   'Pragma': 'no-cache',
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'shannon_spider.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'shannon_spider.middlewares.DBDupeFilterMiddleware': 500,
    # splash
    'scrapy_splash.SplashCookiesMiddleware': 723,
    # splash
    'scrapy_splash.SplashMiddleware': 725,
    'shannon_spider.middlewares.SelectHttpProxyMiddleware': 749,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    # splash
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    #    'example.middlewares.ExampleSpiderMiddleware': 543,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

HTTPPROXY_ENABLED = False

RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]

DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

# splash
SPLASH_URL = 'http://{{ Your Host IP }}:8050/'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'scrapy.pipelines.files.FilesPipeline': 1,
    #'scrapy.pipelines.images.ImagesPipeline': 2,
    'shannon_spider.pipelines.ShannonFilesPipeline': 1,
    'shannon_spider.pipelines.ShannonImagesPipeline': 2,
    'shannon_spider.pipelines.DBPipeline' : 400,
}

FILES_STORE = '/tmp/file' # local storage
IMAGES_STORE = '/tmp/image' # local storage

#FILES_STORE = 'oss://shannon-spider/file' # aliyun oss storage
#IMAGES_STORE = 'oss://shannon-spider/image' # aliyun oss storage

OSS_ACCESS_KEY_ID = '{{ OSS_ACCESS_KEY_ID }}'
OSS_ACCESS_KEY_SECRET = '{{ OSS_ACCESS_KEY_SECRET }}'
OSS_ENDPOINT = '{{ OSS_ENDPOINT }}'
OSS_CONNECT_TIMEOUT = 30

FILES_EXPIRES = -1 # 有效期天数, -1 或None表示永不过期
IMAGES_EXPIRES = -1 # 有效期天数, -1 或None表示永不过期

# robot_spider: dingding 机器人回调链接
ROBOT_SPIDER = ''

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
