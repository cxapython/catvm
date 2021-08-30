'''
文件名：parser.py
功能：解析网页信息，提取相应数据，支持连贯操作，并自动识别时间和url等

接口调用范例：
     print "测试xpath========================================"
    num = Parser("<?xml version=\"1.0\" encoding=\"UTF-8\"?><html><data>12341234</data><time>5分钟前</time></html>").xpath(".//data/text()").int()
    print num
    
    items = Parser("<data>1</data><data>2</data>").xpathall(".//data/text()")
    for item in items:
        print item.int()
        
    print "测试regex========================================="
        
    num = Parser("123412341324abcd").regex("([12]+)").int()
    print num
    
    for item in Parser("123412341324abcd").regexall("([12]+)"):
        print item.int()
        
    print "测试连贯操作=========================================="
    num = Parser("<data>1234.1234abc</data>").xpath("//data/text()").regex("([\d\.]+)").float()
    print num
    
    print "测试时间===================================================="
    print Parser("01月03日 11:16").datetime()
    print Parser("29分钟前").datetime()
    print Parser("今天 15:42").datetime()
    print Parser("2013-11-11 13:52:35").datetime()

    print "测试URL==================================================="
    url = Parser(r"/a.html?b=3&a=4&c=1234134", "http://www.baidu.com/ab/").url()
    print url
'''

import re
from lxml import etree
import datetime, time
from urllib import parse
import urllib
import util

bad_attrs = ['width', 'height', 'style', '[-a-z]*color', 'background[-a-z]*', 'on*']
single_quoted = "'[^']+'"
double_quoted = '"[^"]+"'
non_space = '[^ "\'>]+'
htmlstrip = re.compile("<"  # open
                       "([^>]+) "  # prefix
                       "(?:%s) *" % ('|'.join(bad_attrs),) +  # undesirable attributes
                       '= *(?:%s|%s|%s)' % (non_space, single_quoted, double_quoted) +  # value
                       "([^>]*)"  # postfix
                       ">"  # end
                       , re.I)


def clean_attributes(html):
    while htmlstrip.search(html):
        html = htmlstrip.sub('<\\1\\2>', html)
    return html


class Parser():
    '''
    解析数据类，支持连贯操作
    '''

    def __init__(self, data=None, url='', encoding=None, response=None, clean=None, **kwargs):
        '''
        初始化，data 为页面源码；response就是requests库中的response对象
        '''
        self.response = response
        if not url and response is not None:
            try:
                self.m_url = response.request.url
            except:
                pass
        else:
            self.m_url = url
        self.data = data

        self.clean = clean
        if clean:
            self.data = util.filter_style_script(self.data)

        # 去除xml声明
        self.data = re.sub("^<\?(XML|xml)[^>]+>\s*", "", self.data)

        self.encoding = encoding

        if self.data:
            self._root = etree.HTML(self.data)
            if self.m_url:
                try:
                    self._root.make_links_absolute(self.m_url, resolve_base_href=True)
                except:
                    pass
        else:
            self._root = None

        self.kwargs = kwargs

    def __nonzero__(self):
        '''重载 bool 值 使用 self.data 判断'''
        return bool(self.data)

    def create_Parser(self, data=None, url='', encoding=None, response=None, clean=False, **kwargs):
        """根据传入的字符串创建一个Parser对象 默认使用自身被创建时的参数"""
        data = data if data is not None else self.data
        url = url if url else self.m_url
        encoding = encoding if encoding else self.encoding
        response = response if response is not None else self.response
        clean = clean if clean else self.clean
        kwargs = kwargs if kwargs else self.kwargs
        return Parser(data=data, url=url, encoding=encoding, response=response, clean=clean, **kwargs)

    def xpath(self, xp, default=""):
        '''用xpath，解析data，Parser类实例，用于连贯操作，如果没有解析成功，则返回默认结果'''
        utf8_xp = xp
        try:
            result = self._root.xpath(xp)
        except Exception as e:
            print(util.R("异常：xpath 解析错误: xp is %s; exception:%s; url:%s" % (utf8_xp, e, str(self.m_url))))
            return self.create_Parser(default)

        if len(result) > 0:
            data = result[0]
            return self.create_Parser(etree.tostring(data, encoding=self.encoding, method="html").decode()) if isinstance(data,
                                                                                                                 etree._Element) else self.create_Parser(
                data)
        else:
            print(util.BB("xpath 解析无结果: %s; url: %s" % (utf8_xp, str(self.m_url))))
            return self.create_Parser(default)

    def xpathall(self, xp):
        '''返回多个结果，list方式'''
        utf8_xp = xp
        try:
            result = self._root.xpath(xp)
        except Exception as e:
            print(
                util.R("异常：xpathall 解析错误， xp is %s; exception: %s; url: %s" % (utf8_xp, e, str(self.m_url))))
            return []

        if len(result) > 0:
            return [self.create_Parser(etree.tostring(data, encoding=self.encoding, method="html").decode()) if isinstance(data,
                                                                                                                  etree._Element) else self.create_Parser(
                data) for data in result]
        else:
            print(util.BB("xpathall 解析无结果:  %s;  url: %s" % (utf8_xp, str(self.m_url))))
            return []

    def css(self, cs, default=""):
        '''用xpath，解析data，Parser类实例，用于连贯操作，如果没有解析成功，则返回默认结果'''
        utf8_cs = cs
        try:
            result = self._root.cssselect(cs)
        except Exception as e:
            print(util.R("异常: css 解析错误: css is %s; exception:%s; url:%s" % (utf8_cs, e, str(self.m_url))))
            return self.create_Parser(default)

        if len(result) > 0:
            data = result[0]
            return self.create_Parser(etree.tostring(data, encoding=self.encoding, method="html").decode()) if isinstance(data,
                                                                                                                 etree._Element) else self.create_Parser(
                data)
        else:
            print(util.BB("css 解析无结果: css is %s; url: %s" % (utf8_cs, str(self.m_url))))
            return self.create_Parser(default)

    def cssall(self, cs):
        '''返回多个结果，list方式'''
        utf8_cs = cs
        try:
            result = self._root.cssselect(cs)
        except Exception as e:
            print(
                util.R("异常: cssall 解析错误， css is %s; exception: %s; url: %s" % (utf8_cs, e, str(self.m_url))))
            return []

        if len(result) > 0:
            return [self.create_Parser(etree.tostring(data, encoding=self.encoding, method="html").decode()) if isinstance(data,
                                                                                                                  etree._Element) else self.create_Parser(
                data) for data in result]
        else:
            print(util.BB("cssall 解析无结果: css is %s;  url: %s" % (utf8_cs, str(self.m_url))))
            return []

    def regex(self, reg, default=""):
        '''
        用正则解析data，没有解析成功，则抛出异常，支持连贯操作
        注意：一次只能解析出一个字段
        '''
        utf8_reg = reg
        try:
            result = re.compile(reg).findall(self.data)
        except Exception as e:
            print(
                util.R("异常：regex 解析错误，reg is %s; exception: %s;  url: %s" % (utf8_reg, e, str(self.m_url))))
            return self.create_Parser(default)

        if len(result) > 0:
            data = result[0]
            return self.create_Parser(etree.tostring(data, encoding=self.encoding, method="html").decode()) if isinstance(
            data,
            etree._Element) else self.create_Parser(
            data)
        else:
            print(util.BB("regex 解析无结果: reg is %s; url: %s" % (utf8_reg, str(self.m_url))))
            return self.create_Parser(default)

    def regexall(self, reg):
        '''
        返回list方式的多个结果
        '''
        utf8_reg = reg
        try:
            result = re.compile(reg).findall(self.data)
        except Exception as e:
            print(
                util.R("异常：regexall 解析错误: reg is %s; exception: %s; url: %s" % (utf8_reg, e, str(self.m_url))))
            return []

        if len(result) > 0:
            return [
                self.create_Parser(etree.tostring(data, encoding=self.encoding, method="html").decode()) if isinstance(
                    data,
                    etree._Element) else self.create_Parser(
                    data) for data in result]
        else:
            print(util.BB("regexall 解析无结果: reg is %s;  url: %s" % (utf8_reg, str(self.m_url))))
            return []

    def strip(self):
        '''
        删除空格等，等效于python的strip()函数，只是支持连贯操作
        '''
        try:
            data = self.data.strip()
            data = re.sub(r'(&#160;)+$', '', data)
        except Exception as e:
            print("异常：strip错误，%s" % e)
            return self.create_Parser(self.data)

        return self.create_Parser(data)

    def str(self, encoding="utf8"):
        '''
        把data转为字符串，默认返回utf8编码，解析出来结果是多个，例如xpath，则只是提取一个，如果是多个，需要用tuple()处理
        '''
        return self.data.encode(encoding)

    def text(self, encoding="utf8"):
        '''
        提取data代表的标签内的text，默认返回utf8编码;与str()函数的不同之处在于，该函数操作在基于html文档的etree element之上；
        而str()函数只是对文本内容进行编码
        '''
        return etree.tostring(self._root, encoding=encoding, method='text').decode() if self._root is not None else ''

    def html(self, encoding="utf8"):
        '''
        '''
        return etree.tostring(self._root, encoding=encoding, method='html').decode() if self._root is not None else ''

    def cleaned_html(self, encoding="utf8"):
        '''
        '''
        return self.html(encoding=encoding)

    def int(self, default=-1):
        '''
        把data转为整数，如果不全是数字，例如：123abc，则抛出异常
        '''
        result = default
        try:
            result = int(self.data)
        except Exception as e:
            print("异常：int转换错误,%s" % e)
        return result

    def float(self, default=0.0):
        '''
        把data转为浮点，如果转换不成功，则抛出异常
        '''
        result = default
        try:
            result = float(self.data)
        except Exception as e:
            print("异常：float转换错误，%s" % e)
        return result

    def datetime(self):
        '''
        把data转换为日期时间，时区为东八区北京时间，能够识别：今天、昨天、5分钟前等等，如果不能成功识别，则返回None
        '''
        return util.utc_datetime(self.data)

    def url(self, remove_param=False):
        '''
        把data转换为标准的url格式，如果url有参数，则按照升序重新排列，防止url相同，但是参数顺序不同而造成的url不同的识别错误，
        例如http://xxx.com/123.html?b=1&a=3，则返回http://xxx.com/123.html?a=3&b=1；
        如果remove_param=True，则删除参数，例如http://xxx.com/123.html?b=1&a=3，则返回为http://xxx.com/123/html；
        如果是相对路径，例如123.html，则返回绝对路径：http://xxx.com/123.html，并识别/123.html,则为http://xxx.com/123.html
        注意：识别url需要在__init__中设置url参数，否则无法识别相对路径的Url
        '''

        result = ""

        uri = parse.urlsplit(self.data)
        # 对参数进行排序，名字升序
        query = parse.parse_qsl(uri.query, True)
        query.sort()
        query = urllib.parse.quote(query)

        if uri.netloc == "":
            # 没有域名
            result = parse.urljoin(self.m_url,
                                      parse.urlunsplit((uri.scheme, uri.netloc, uri.path, query, uri.fragment)))
        else:
            result = parse.urlunsplit((uri.scheme, uri.netloc, uri.path, query, uri.fragment))

        return result

    def replace(self, pattern, repl, count=0):
        """
        将data中满足规则pattern的元素替换为字符串repl; 
        参数count表示替换发生的最大次数；必须为非负整数；默认为0,表示替换所有符合条件的元素；
        """
        try:
            result = re.compile(pattern).sub(repl, self.data, count)
        except Exception as e:
            print("异常：replace 替换错误，%s" % e)
            return self

        return self.create_Parser(result)

    def delete(self, pattern, count=0):
        """
        删除data中符合规则pattern的元素；参数count同sub
        """
        try:
            result = re.compile(pattern).sub("", self.data, count)
        except Exception as e:
            print("异常: delete 删除出现错误: %s" % e)
            return self

        return self.create_Parser(result)

    def urls(self, base_url, domains=None, regex=None):
        """
        找出所有的有效url;
        参数base_url代表url前缀，用来生成绝对url; 参数domains指允许的url域；regex是一个正则表达式，用来过滤url;
        """
        try:
            result = etree.HTML(self.data).xpath("//a/@href | //iframe/@src")
        except Exception as e:
            print("异常：xpath 解析错误， %s" % e)
            return []
        # 去重
        urls_set = set(result)

        if regex is not None:
            reg = re.compile(regex, re.U)
        urls = []
        for url in urls_set:
            if regex is not None:
                try:
                    res = reg.findall(url)
                except Exception as e:
                    print("异常：findall in urls() 解析错误， %s" % e)
                    continue
                if res:
                    url = res[0]
                else:
                    continue
            if str(url).startswith("/"):
                if base_url is not None:
                    url = base_url + url
                    urls.append(url)
                elif self.m_url is not None:
                    url = self.m_url + url
                    urls.append(url)
                else:
                    continue
            elif url.startswith(("http://", "https://")):
                uri = parse.urlsplit(url)
                if domains is not None:
                    if uri.netloc and uri.netloc in domains:
                        urls.append(url)
                else:
                    urls.append(url)
        return urls

    def remove(self, xp):
        '''去除指定xpath对应的数据 返回一个不包含已去除数据的'''
        _root = etree.HTML(self.data)
        try:
            result = _root.xpath(xp)
            for r in result:
                r.getparent().remove(r)
        except Exception as e:
            print(util.R("异常：xpath 解析错误: xp is %s; exception:%s; url:%s" % (xp, e, str(self.m_url))))
            return self
        return self.create_Parser(etree.tostring(_root, encoding=self.encoding, method="html"))

    def utcnow(self):
        return datetime.datetime.utcnow()

    def fromtimestamp(self):
        return datetime.datetime.fromtimestamp(float(self.data)) - datetime.timedelta(hours=8)

