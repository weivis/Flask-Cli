# coding=utf-8

"""
    个人常用工具包
    update 20201227
    ver 0.3
"""

from random import Random
import datetime
import re
import math
import time
import hashlib

def calc_crc16(data, len):
    """生成CRC16校验码"""
    data = bytearray.fromhex(data)
    # print(data)
    crc = 0xFFFF
    for pos in range(0, len):
        crc ^= data[pos]
        for i in range(8):
            if (crc & 1) != 0:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return ((crc & 0xff) << 8) + (crc >> 8)


def HextoStr(data):
    """十六进制转字符串"""
    data = binascii.a2b_hex(data)
    data = text.decode(encoding='utf-8')
    return data


def GenerateRandomHex(len=12):
    """生成16进制随机值
    Args:
        len 长度
    Returns:
        value
    """
    return "".join([choice("0123456789ABCDEF") for i in range(len)])

def StrtoHex(str):
    """字符串转16进制
    """
    str = binascii.b2a_hex(str.encode("utf8"))
    str = str.decode(encoding='utf-8')
    return str


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


def _Paginate(querys, query_page, pagesize=10):
    """Sqlachamy query预处理

    Args:
        querys: 查询集
        query_page: int, 需要获取的页数, 默认1
        pagesize: int, 每页显示条目个数, 默认10

    Returns: 
        1.total 条目数
        2.result 生成器
        3.currentPage 当前页数
        4.pageCount 总页数

    Example:
        querypage = request.get('querypage',1)
        pagesize = request.get('pagesize',10)

        querys = XXX.query.filter()

        querys = querys.order_by(XXX.create_time.desc())
        total, result, currentPage, pageCount = _Paginate(querys, querypage, pagesize)

        return 200, "", {
            "total":total,
            "result":[i.toDict() for i in result],
            "currentPage":currentPage,
            "pageCount":pageCount
        }
    """
    if query_page == 0:
        query_page = 1
    total = querys.count()
    _paginate = querys.paginate(
        query_page, per_page=pagesize, error_out=False)  # 查询的页数, 每页的条数
    """
    error_out 当值为 True 时，下列情况会报错
        当 page 为 1 时，找不到任何数据
        page 小于 1，或者 per_page 为负数
        page 或 per_page 不是整数
    该方法返回一个分页对象 Pagination
    """
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
