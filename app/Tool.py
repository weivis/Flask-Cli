# coding=utf-8

"""
    个人常用工具包
    update 20201002
    ver 0.1
"""

from random import Random
import datetime
import re
import math
import time
import hashlib

def RandomStr(randomlength=8):
    """生成随机字符串
    Args:
        randomlength: int 随机字符串长度 默认长度8位
    Returns:
        str
    """
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str   # 将拼接的字符串返回


def T_Stamp():
    """获取时间戳"""
    return int(time.time())


def CheckEmailStr(email):
    """检验字符串是否合法邮箱格式
    Args:
        email: str 
    Returns:
        True, False
    """
    # re.compile(r"\"?([a-zA-Z0-9_-]+@\w+\.\w+)\"?")
    pattern = re.compile(r"\"?([0-9A-Za-z\-_\.]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


def Paginator(data, page, num=10):
    """
    列表分页(切片列表, 数据总量，分页总页数)

    Args:
        data: list 需要分页的数据的列表
        page: int 获取页数
        num: int 分页数 默认为10

    Returns:
        列表: item
        总条数: 总数量
        分页数: 总页数/每页条数 = 分页数
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

    Args:
        querys: 查询集
        query_page: int 需要获取的页数

    Returns: 
        1.一共查询到的数量(count)
        2.查询集对象 list
        3.当前页数 currentPage
        4.totalPages 总页数
        example:
        
            return count, _paginate.items, _paginate.page, _paginate.pages
            total, result, currentPage, totalPages = _Paginate(a,b)

    Example:
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
    """字符串转DATE

    用于接收前端发送的日期字符串并转换为date用于程序使用

    Args:
        s: str, Yyyy-MM-dd 格式

    Returns: 
        :Returns Date
    """
    try:
        year_s, mon_s, day_s = s.split('-')
        return datetime.datetime(int(year_s), int(mon_s), int(day_s))
    except Exception as e:
        print(e)
        return {}


def CNSpendTime(time):
    """返回中文的度过时间

    Args:
        time: datetime, 需要计算度过了多久的时间

    Returns: 
        Str: {}'秒前', {}'分钟', {}'小时前', {}'天前', {}'周前', {}'月前', {}'年前'

    """
    sout = datetime.datetime.now() - time
    timetype_seconds = datetime.timedelta(seconds=60)
    timetype_hour = datetime.timedelta(hours=1)
    timetype_days = datetime.timedelta(days=1)
    timetype_weeks = datetime.timedelta(weeks=1)
    timetype_month = datetime.timedelta(days=30)
    timetype_year = datetime.timedelta(days=365)

    if sout < timetype_seconds:
        return str(int(sout.seconds)) + '秒前'

    if sout < timetype_hour:
        return str(int(sout.seconds / 60)) + '分钟'

    elif sout < timetype_days:
        return str(int(sout.seconds / 60 / 60)) + '小时前'

    elif sout < timetype_weeks:
        return str(int(sout.days)) + '天前'

    elif sout < timetype_month:
        return str(int(sout.days / 7)) + '周前'

    elif sout < timetype_year:
        return str(int(sout.days / 30)) + '月前'

    else:
        return str(int(sout.days / 365)) + '年前'


def GenerateIdentification(material):
    """生成数据的唯一标识
    Args:
        material: str,生成材料

    Returns: 
        str: RandomStr + material + T_Stamp
    """
    return str(RandomStr() + str(material) + str(T_Stamp()))


def GenerateToken(plaintext=None):
    """生成Token

    生成规则, md5(plaintext + T_Stamp + RandomStr)

    Args:
        plaintext: str, 自定义字符串

    Returns: 
        str
    """
    sourcestr = plaintext + str(T_Stamp()) + RandomStr()
    print(plaintext, sourcestr)
    return str(hashlib.md5(sourcestr.encode("utf8")).hexdigest())
