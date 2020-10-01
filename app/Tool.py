#coding=utf-8

"""
    个人常用工具包
    :update 20201002
    :ver 0.1
"""

from random import Random
from datetime import datetime
import re
import math

def RandomStr(randomlength=8):
    """生成随机字符串

    :param randomlength :int 随机字符串长度 默认长度8位
    """
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str   # 将拼接的字符串返回

def CheckEmailStr(email):
    """检验字符串是否合法邮箱格式

    :param email :str 
    正确情况下返回True
    """
    # re.compile(r"\"?([a-zA-Z0-9_-]+@\w+\.\w+)\"?")
    pattern = re.compile(r"\"?([0-9A-Za-z\-_\.]+@\w+\.\w+)\"?")
    return re.match(pattern, email)

def Paginator(data, page, num=10):
    """
    列表分页(切片列表, 数据总量，分页总页数)

    :param data :list 需要分页的数据的列表
    :param page :int 获取页数
    :param num  :int 分页数 默认为10
    
    :return :列表
    :return :总条数
    :return :分页数
    """
    num = num
    page = page
    total = len(data)
    pages = math.ceil(total/num)
    ret = []
    if num*page < total:
        for i in range((page-1)*num, num*page):
            ret.append(data[i])
    elif (page-1)*num < total <= num*page:
        for i in range((page-1)*num, total):
            ret.append(data[i])

    return ret, total, pages

def _Paginate(querys, query_page, per_page=10):
    """Sqlachamy query预处理

    Args
        :param querys : 查询集
        :param query_page : 需要获取的页数

    Returns 
        1.一共查询到的数量(count)
        2.查询集对象 list
        3.当前页数 currentPage
        4.totalPages 总页数
        # return count, _paginate.items, _paginate.page, _paginate.pages
        :Returns total, result, currentPage, totalPages

    Ues
        query_page = request.get('query_page',1)
        total, result, currentPage, totalPages = _Paginate(querys, query_page)
        "total":total,
        "result":result,
        "currentPage":currentPage,
        "totalPages":totalPages
    """
    if query_page == 0:
        query_page = 1
    total = querys.count()
    _paginate = querys.paginate(query_page, per_page=per_page, error_out=False)
    return total, _paginate.items, _paginate.page, _paginate.pages

def StrForDate(s):
    """
        字符串转DATE

        :param s :str, Yyyy-MM-dd 格式
        :Returns Date
    """
    try:
        year_s, mon_s, day_s = s.split('-')
        return datetime(int(year_s), int(mon_s), int(day_s))
    except Exception as e:
        print(e)
        return {}