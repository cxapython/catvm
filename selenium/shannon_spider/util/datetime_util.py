# coding=utf-8

import time
import datetime
# from dateutil.relativedelta import relativedelta

month_contrast = {
    '01': 31,
    '02': 28,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31
}


def get_now_time(layout='%Y-%m-%d %H:%M:%S'):
    """获取当前时间"""
    return datetime.datetime.now().strftime(layout)


def get_now_year():
    """获取当前所在年份"""
    return datetime.datetime.now().year


def times2date(timestamp, layout='%Y-%m-%d %H:%M:%S'):
    """时间戳转换本地日期"""
    time_array = time.localtime(timestamp)
    local_date = time.strftime(layout, time_array)
    return local_date


def date2stamp(date, layout='%Y-%m-%d %H:%M:%S'):
    """格式化时间转换时间戳"""
    time_array = time.strptime(date, layout)
    time_stamp = int(time.mktime(time_array))
    return time_stamp


def date_add_year(str_time, n=1, layout='%Y-%m-%d %H:%M:%S'):
    """日期增加或减少n年"""
    try:
        local_time = datetime.datetime.strptime(str_time, '%Y-%m-%d')
    except ValueError:
        local_time = datetime.datetime.strptime(str_time, layout)
    years = datetime.timedelta(days=364 * n)
    return (local_time + years).strftime(layout)


def date_add_month(str_time, n=1, layout='%Y-%m-%d %H:%M:%S'):
    """日期增加或减少n月"""
    try:
        local_time = datetime.datetime.strptime(str_time, '%Y-%m-%d')
    except ValueError:
        local_time = datetime.datetime.strptime(str_time, layout)
    # 需要安装dateutil, 开发环境中未安装fuck了
    # month = relativedelta(months=n)

    # 判断是否是闰年
    year = str(local_time)[0:4]
    if int(year) % 4 == 0 and int(year) % 100 != 0:
        is_year = True
    elif int(year) % 400 == 0:
        is_year = True
    else:
        is_year = False
    # 判断月份
    month = str(local_time)[5:7]
    v = month_contrast.get(str(month))
    if month == '02' and is_year:
        v += 1
    month = datetime.timedelta(days=v * n)
    return (local_time + month).strftime(layout)


def date_add_day(str_time, n=1, layout='%Y-%m-%d %H:%M:%S'):
    """日期增加或减少n天"""
    try:
        local_time = datetime.datetime.strptime(str_time, '%Y-%m-%d')
    except ValueError:
        local_time = datetime.datetime.strptime(str_time, layout)
    days = datetime.timedelta(days=n)
    return (local_time + days).strftime(layout)


def date_compare(str_time, current_time=None):
    """current_time和str_time进行比较"""
    str_time = datetime.datetime.strptime(str_time, '%Y-%m-%d')
    if not current_time:
        current_time = get_now_time(layout='%Y-%m-%d')
    current_time = datetime.datetime.strptime(current_time, '%Y-%m-%d')
    return current_time > str_time


def timestamp2local(timestamp, layout='%Y-%m-%d %H:%M:%S'):
    """时间戳格式化"""
    time_array = time.localtime(timestamp)
    local_time = time.strftime(layout, time_array)
    return local_time


def make_date(start_time):
    # 够造请求日期（需将2006-10-8至现在所有数据爬取）
    # 请求数据日期规格只能为一年，即2006-10-08至2007-10-07
    # start_time = '2006-10-08'
    # return [{'start_time': '2006-10-08', 'end_time': '2007-10-07'}.....]
    date_list = []
    start_time = start_time
    end_time = date_add_year(str_time=start_time, layout='%Y-%m-%d')
    while 1:
        if not date_compare(end_time):
            end_time = get_now_time(layout='%Y-%m-%d')
            item = {
                'start_time': date_list[-1]['end_time'],
                'end_time': end_time
            }
            date_list.append(item)
            break
        item = {
            'start_time': start_time,
            'end_time': end_time
        }
        date_list.append(item)
        start_time = item['end_time']
        end_time = date_add_year(str_time=start_time, layout='%Y-%m-%d')
    return date_list


def make_date_for_month_dict(start_time):
    # start_time = '2006-06-01'
    # return [{'start_time': '2006-06-01', 'end_time': '2006-07-01'}.....]
    date_list = []
    start_time = start_time
    end_time = date_add_month(str_time=start_time, layout='%Y-%m-%d')
    while 1:
        if not date_compare(end_time):
            end_time = get_now_time(layout='%Y-%m-%d')
            item = {
                'start_time': date_list[-1]['end_time'],
                'end_time': end_time
            }
            date_list.append(item)
            break
        item = {
            'start_time': start_time,
            'end_time': end_time
        }
        date_list.append(item)
        start_time = item['end_time']
        end_time = date_add_month(str_time=start_time, layout='%Y-%m-%d')
    return date_list


def make_date_for_month(start_time, end_time=None):
    """获取开始日期到结束日期所有时间(按月递增)"""
    date_list = []
    if not end_time:
        end_time = get_now_time()
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d').strftime('%Y-%m-%d')
    while 1:
        save_date = date_add_month(start_time, layout='%Y-%m-%d')
        if save_date > end_time:
            break
        date_list.append(save_date)
        start_time = save_date
    return date_list


def make_date_for_day(start_time, end_time=None):
    """获取开始日期到结束日期所有时间(按月递增)"""
    date_list = []
    if not end_time:
        end_time = get_now_time(layout='%Y-%m-%d')
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d').strftime('%Y-%m-%d')
    date_list.append(start_time)
    while 1:
        save_date = date_add_day(start_time, layout='%Y-%m-%d')
        if save_date > end_time:
            break
        date_list.append(save_date)
        start_time = save_date
    return date_list

def creat_timestamp_ms():
    '''获取毫秒级时间戳'''
    return int(round(time.time() * 1000))


