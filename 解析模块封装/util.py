import re
import sys
import copy
import datetime
import html

from lxml.html.clean import Cleaner

try:
    from termcolor import colored
except ImportError:
    def colored(text, color=None, on_color=None, attrs=None):
        return text

is_py3 = sys.version_info.major == 3


def clear_special_xpath(data, xp):
    '''
    删除指定 xpath 数据
    仅作用于 htmlparser.Parser 对象
    '''
    data = copy.deepcopy(data)
    result = data._root.xpath(xp)
    try:
        for i in result:
            i.getparent().remove(i)
    except:
        pass
    return data


def filter_style_script(text):
    '''去除注释 style script'''
    html_cleaner = Cleaner(scripts=True, javascript=True, comments=True, style=True,
                           links=False, meta=False, page_structure=False, processing_instructions=False,
                           embedded=False, frames=False, forms=False, annoying_tags=False, remove_tags=None,
                           remove_unknown_tags=False, safe_attrs_only=False)
    text = html_cleaner.clean_html(text)
    return text


def text_to_str(text, encoding='utf8'):
    '''
    将传入文本转换为str类型 兼容py2 py3
    '''
    if is_py3:
        if isinstance(text, bytes):
            text = text.decode(encoding)
    return text


def local_datetime(data):
    '''
    把data转换为日期时间，时区为东八区北京时间，能够识别：今天、昨天、5分钟前等等，如果不能成功识别，则返回datetime.datetime.now()
    '''
    dt = datetime.datetime.now()
    # html实体字符转义
    data = html.unescape(data)
    data = data.strip()
    if not data:
        return dt
    try:
        data = text_to_str(data)
    except Exception as e:
        print("utc_datetime() error: data is not utf8 or unicode : %s" % data)

    # 归一化
    data = data.replace("年", "-").replace("月", "-").replace("日", " ").replace("/", "-").strip()
    data = re.sub("\s+", " ", data)

    year = dt.year

    regex_format_list = [
        # 2013年8月15日 22:46:21
        ("(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M:%S", ""),

        # "2013年8月15日 22:46"
        ("(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M", ""),

        # "2014年5月11日"
        ("(\d{4}-\d{1,2}-\d{1,2})", "%Y-%m-%d", ""),

        # "2014年5月"
        ("(\d{4}-\d{1,2})", "%Y-%m", ""),

        # "13年8月15日 22:46:21",
        ("(\d{2}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})", "%y-%m-%d %H:%M:%S", ""),

        # "13年8月15日 22:46",
        ("(\d{2}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2})", "%y-%m-%d %H:%M", ""),

        # "8月15日 22:46:21",
        ("(\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M:%S", "+year"),

        # "8月15日 22:46",
        ("(\d{1,2}-\d{1,2} \d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M", "+year"),

        # "8月15日",
        ("(\d{1,2}-\d{1,2})", "%Y-%m-%d", "+year"),

        # "3 秒前",
        ("(\d+)\s*秒前", "", "-seconds"),

        # "3 秒前",
        ("(\d+)\s*分钟前", "", "-minutes"),

        # "3 秒前",
        ("(\d+)\s*小时前", "", "-hours"),

        # "3 秒前",
        ("(\d+)\s*天前", "", "-days"),

        # 今天 15:42:21
        ("今天\s*(\d{1,2}:\d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M:%S", "date-0"),

        # 昨天 15:42:21
        ("昨天\s*(\d{1,2}:\d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M:%S", "date-1"),

        # 前天 15:42:21
        ("前天\s*(\d{1,2}:\d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M:%S", "date-2"),

        # 今天 15:42
        ("今天\s*(\d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M", "date-0"),

        # 昨天 15:42
        ("昨天\s*(\d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M", "date-1"),

        # 前天 15:42
        ("前天\s*(\d{1,2}:\d{1,2})", "%Y-%m-%d %H:%M", "date-2"),
    ]

    for regex, dt_format, flag in regex_format_list:
        m = re.search(regex, data)
        if m:
            if not flag:
                dt = datetime.datetime.strptime(m.group(1), dt_format)
            elif flag == "+year":
                # 需要增加年份
                dt = datetime.datetime.strptime("%s-%s" % (year, m.group(1)), dt_format)
            elif flag in ("-seconds", "-minutes", "-hours", "-days"):
                # 减秒
                flag = flag.strip("-")
                exec("dt = dt - datetime.timedelta(%s=int(m.group(1)))" % flag)
            elif flag.startswith("date"):
                del_days = int(flag.split('-')[1])
                _date = dt.date() - datetime.timedelta(days=del_days)
                _date = _date.strftime("%Y-%m-%d")
                dt = datetime.datetime.strptime("%s %s" % (_date, m.group(1)), dt_format)
            return dt
    else:
        print("unknow datetime format: %s" % data)
    return dt


def utc_datetime(data):
    try:
        utc_dt = local_datetime(data) - datetime.timedelta(hours=8)
    except Exception as e:
        utc_dt = datetime.datetime.utcnow()
        print(e)
    return utc_dt


def R(x):
    return colored(x, 'red', attrs=['bold'])


def G(x):
    return colored(x, 'green', attrs=['dark', 'bold'])


def B(x):
    return colored(x, 'blue', attrs=['bold'])


def Y(x):
    return colored(x, 'yellow', attrs=['dark', 'bold'])


def RR(x):
    return colored(x, 'white', 'on_red', attrs=['bold'])


def GG(x):
    return colored(x, 'white', 'on_green', attrs=['dark', 'bold'])


def BB(x):
    return colored(x, 'white', 'on_blue', attrs=['bold'])


def YY(x):
    return colored(x, 'white', 'on_yellow', attrs=['dark', 'bold'])
