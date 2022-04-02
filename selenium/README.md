## 目标
我们所用的爬虫是专用爬虫，并且抓取的数据不会频繁变动，所以速度并不是最重要的，稳定地增量抓取才是最重要的。
所以单一爬虫的访问频次不宜太高，吞吐量不宜过大。

## 功能描述
本框架是基于 [scrapy](https://github.com/scrapy/scrapy) ，在 [scrapyd](https://github.com/scrapy/scrapyd) 上执行，用 [spiderkeeper](https://github.com/jiweil/SpiderKeeper) 调度和监控。以下是目前支持的主要功能：

- **自动选择代理**

1. 在 `settings.py` 中添加以下配置


    ```python
    DOWNLOADER_MIDDLEWARES = {
        'shannon_spider.middlewares.SelectHttpProxyMiddleware': 749,
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    }
    HTTPPROXY_ENABLED = True
    ```

    > 要启用自动代理功能，要同时开启`SelectHttpProxyMiddleware` 和 `HttpProxyMiddleware`, 前者用来选择proxy，后者用来解析proxy. 采用这种方式，是为了和scrapy自身的代理设置功能保持兼容.

1. 在`conf/proxy.py`中添加以下配置：

    ```python
    # 每个代理连续使用的请求数，默认为3
    CONTINUOUS_USE_COUNT = 10

    PROXY_LIST = [
        'local_direct_connect',
        #'http://127.0.0.1:3128',
    ]
    ```

- **自动选择user-agent**

1. 在 `settings.py` 中添加以下配置

    ```python
    DOWNLOADER_MIDDLEWARES = {
        'shannon_spider.middlewares.RandomUserAgentMiddleware': 400,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    }
    ```

    > 上面的 middleware 配置之后，会自动开启自动选择user-agent功能. 注意要禁用系统自带的 `UserAgentMiddleware`

1. 在`conf/user_agent.py`中添加以下配置：

    ```python
    USER_AGENT_LIST = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    ]
    ```

- **会话保持**


1. 在 `settings.py` 中添加以下配置

    ```python
    COOKIES_ENABLED = True
    ```

    > 复用 scrapy 的 cookie 保持功能

- **url 去重**

1. 在 `settings.py` 中添加以下配置

    ```python
    DOWNLOADER_MIDDLEWARES = {
        'shannon_spider.middlewares.DBDupeFilterMiddleware': 500,
    }
    DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'
    ```

    > `DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'` 用于禁用scrapy 默认的过滤中间件。因为scrapy的过滤器是单次有效的.
    `DBDupeFilterMiddleware` 将抓取记录保存在mysql数据库表中，访问之前要读历史数据库，并根据url，post_data, expire 等进行去重

- **抓取结果自动保存及更新**

1. 在 `settings.py` 中添加以下配置

    ```
    ITEM_PIPELINES = {
        'shannon_spider.pipelines.DBPipeline' : 400,
    }
    ```

    > 爬虫将采集结果保存到 ShannonCrawledItem 对象中，这个pipeline将自动保存结果对应的item，以及历史记录。并自动处理数据过期更新的情况。

- **文件/图片自动保存及更新**

1. 在 `settings.py` 中添加以下配置

    ```
    ITEM_PIPELINES = {
        'shannon_spider.pipelines.ShannonFilesPipeline': 1,
        'shannon_spider.pipelines.ShannonImagesPipeline': 2,
    }
    ```

    > 1. 支持将文件和图片保存到本地文件系统和 oss 中，可以在settings.py 中通过 `FILES_STORE` 和 `IMAGES_STORE` 配置.
    > 1. 之所以将文件和图片分开是为了复用scrapy的图片处理功能（裁剪，格式转换, 根据尺寸进行过滤等）
    > 1. 文件的更新包含两层：首先，如果 url 没有过期，文件也不会更新; url 过期之后，会根据文件的last_modified 时间判断是否需要更新。
    > 1. 要下载的文件和图片分别被封装在 `FileUri` 和 `ImageUri` 中。支持自定义文件名和后缀名。


## 爬虫开发指南
爬虫位于 `shannon_spider/spiders` 目录下，下面将以`cde`为例：

1. 设置数据库
    本框架采用 `sqlalchemy` 作为存储后端，要设置数据库连接和数据库，请在 `settings.py` 中添加以下配置：

    ```python
    CRAWLED_DATABASE  = 'mysql+pymysql://db_user:db_passwd@localhost/crawl_result?charset=utf8'
    ECHO_SQL = False
    ```

    > 修改这个配置主要是为了方便本地调试。`ECHO_SQL = True` 可以打印出查询所用 sql。

2. 定义抓取结果 Item，即 sqlalchemy 的表

    ```python
    from shannon_spider.db import CommonFieldMixin, ItemBaseModel

    class CdeNewsItem(CommonFieldMixin, ItemBaseModel):
        '''保存新闻的抓取结果'''
        __tablename__ = 'cde_news'
        desc = 'cde 要闻导读'
        title = Column(String(200))
        date = Column(Date)
        content = Column(TEXT)
        images = Column(TEXT)
        url = Column(String(300))
    ```

    > 1. `CommonFieldMixin` 包含一些公用的字段，目前只有一个主键 `id`。用户只需要设置表名，关注要抓取的字段即可。
    > 1. 为了保持爬虫模块的独立性，大段文本目前仍然是保存在 mysql 中的，后面根据需求看是否需要添加到`elastic search`中。


    > 当用命令`scrapy crawl cde`启动爬虫时，框架自动在 `crawl_result` 数据库中创建两个表: `cde_news`（称为result table） 和 `cde_news_history` （称为 history table）。其中前者用来保存抓取结果，后者用来保存抓取历史记录和url的过期时间，主要是用于避免重复访问已经抓取成功的 url。

    history table 的表模式如下:

    ```
    +--------------+---------------+------+-----+-------------------+-----------------------------+
    | Field        | Type          | Null | Key | Default           | Extra                       |
    +--------------+---------------+------+-----+-------------------+-----------------------------+
    | id           | int(11)       | NO   | PRI | <null>            | auto_increment              |
    | url_sha      | char(40)      | NO   | MUL | <null>            |                             |
    | req_repr     | varchar(1024) | NO   |     | <null>            |                             |
    | last_updated | timestamp     | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
    | expire       | int(11)       | NO   |     | -1                |                             |
    +--------------+---------------+------+-----+-------------------+-----------------------------+
    ```

    > - url_sha 是根据 url + post_data 计算出来的SHA（可能重复），主要用于快速检索
    > - req_repr 是请求的 json 表示（不会重复）
    > - last_updated 是最后一次更新时间
    > - expire 指定多少秒之后过期（默认为-1，表示永不过期，0 表示每次都更新）
    > 通常情况下，用户不需要关心这个表的具体内容。

3. 写爬虫

    ```python
    class CdeSpider(ShannonBaseSpider):
        # 以下是基类定义的属性
        name = 'cde'
        result_orm_model = CdeNewsItem

        allowed_domains = ['cde.org.cn']
        start_urls = ['http://www.cde.org.cn/news.do?method=news_index&frameStr=3']
        custom_settings = {}

        def build_orm_item(self, item: ShannonCrawledItem):
            '''
            将dict类型的item转成orm item
            '''
            orm_item = CdeNewsItem()
            orm_item.title = item['title']
            orm_item.date = datetime.strptime(item['date'], "%Y%m%d").date()
            orm_item.content = item['content']
            orm_item.url = item['url']
            orm_item.images = '\t'.join([image['path'] for image in item['images'] if image])
            return orm_item

        def parse(self, response):
            ...
            request = scrapy.Request(url=self.navigation_page_url, callback=self.parse_navigation_page)
            request.meta['use_dup_filter'] = False
            yield request

        def parse_navigation_page(self, response):
            ...
            request = scrapy.FormRequest(url=self.list_page_url, formdata=post_data, callback=self.parse_list_page)
            request.meta['use_dup_filter'] = False
            yield request

        def parse_list_page(self, response):
            ...
            yield response.follow(href, callback=self.parse_detail_page, meta={'use_dup_filter': True})

        def parse_detail_page(self, response):
            ...
            image_urls = [ImageUri(response.urljoin(url)) for url in response.xpath('//table/tr/td/*/img/@src').extract()]
            item = ShannonCrawledItem(self, response) # 创建 ShannonCrawledItem 对象
            item['url'] = response.request.url
            item['title'] = title
            item['date'] = date
            item['content'] = content
            item['image_urls'] = image_urls
            yield item
    ```

    > - ShannonBaseSpider: 所有爬虫的基类。
    > - name: 爬虫的名称
    > - result_orm_model : 即 result table
    > - allowed_domains: 这个爬虫允许的访问范围
    > - start_urls: 起始url，可以是一个list
    > - custom_settings: 可以写爬虫特定配置，将覆盖 `settings.py` 中的配置
    > - build_orm_item: 所有爬虫必须重写这个函数。item 是 `ShannonCrawledItem` 类型的对象，其中保存了抓取结果。这个函数的作用就是把 `ShannonCrawledItem` 转成可以保存到数据库中的 ORM item.
    > - parse: 所有爬虫必须重写这个函数。scrapy拿到响应之后，会默认回调parse函数。
    > - request.meta['use_dup_filter']: 是否对这个 request 启用过滤. 通常导航页，列表页不进行过滤，包含抓取结果的详情页要启用过滤。默认为 False。
    > - 通常用 [xpath](http://zvon.org/xxl/XPathTutorial/General/examples.html) 对网页解析

4. 下载文件或图片

    用户只需要将要下载的文件或图片分别放在`ShannonCrawledItem['file_urls']`  和 `ShannonCrawledItem['image_urls']` 即可。如：

    ```python
    item['image_urls'] = [ImageUri(response.urljoin(url)) for url in response.xpath('//table/tr/td/*/img/@src').extract()] 
    ```

    ImageUri 的定义如下：

    ```python
    class ImageUri(NamedTuple):
        url: str
        name: str = None
        ext: str = None
    ```

    > - image资源
    > - url: 资源链接
    > - name: 自定义文件名, 不包含扩展名
    > - ext: 资源扩展名, 默认为 None
    > - FileUri 类似

    框架下载文件完成之后，会将文件和图片的下载结果分别放在`ShannonCrawledItem['files']`，`ShannonCrawledItem['images']` 中。格式如下：

    ```python
        [(True, {'checksum': 'md5_checksum',
              'path': 'oss://images/cde/file_name.jpg',
              'url': 'http://www.example.com/files/product1.pdf'}),
         (False,Failure(...))
        ]
    ```

    > 更详细内容可参考 [Downloading and processing files and images](https://doc.scrapy.org/en/latest/topics/media-pipeline.html)

5. 部署
    爬虫需要部署到 spiderkeeper 上， 再由 spiderkeeper 部署到 scrapyd 上，我们需要做的只是前一步，后一步由 spiderkeeper 自动完成

    > - 首先启动scrapd服务，切换到 scrapyd 目录，执行
    ```shell
        docker-compose up
    ```
    > - 然后启动spiderkeeper，切换到 SpiderKeeper git Repo下，执行
    ```python
        python Spiderkeeper/run.py
    ```
    > - 接下来从 http://spiderkeeper.shannonai.com/project/manage 创建 shannon_spider 项目
        Create Project -> 输入项目名称shannon_spider
    > - 最后生成 shannon_spider 项目的 egg 包，上传到 spiderkeeper，切换到 shannon_spider git Repo，执行
    ```python
        python deploy.py
    ```
        部署过程中会把 egg 包传给 spiderkeeper 作为一个爬虫项目的记录；上传完毕后，会自动删除部署过程中产生的文件

6. 管理：从浏览器访问 http://spiderkeeper.shannonai.com

    可以通过图形界面管理爬虫，主要有两种模式：
    > - Dashboard -> Run Once -> 选择要运行的爬虫，设置任务优先级
    > - Periodic Jobs -> Add Job -> 选择爬虫名称，设置任务优先级、定时
    创建爬虫运行任务后，可以进行 enable、disable、run、remove 等操作
    
7.