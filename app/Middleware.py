#coding=utf-8
from functools import wraps
from flask import request
from app.Common import ReturnRequest
from app.Models import AccountAdmin, AccountUser
from app.Config import BaseConfig

def POST(func=None):
    """通用Post请求"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            return func(request, *args, **kwargs)
        else:
            return ReturnRequest(405,'请求方法不对','')
    return wrapper

def TOKEN(permission):
    """
    Token验证
    
    请求时头部['headers'] 需要携带 'Authorization' 参数名 并传入token

    Args:
        permission: int, 设置允许访问的请求token类型, 1管理员, 2一般用户

    Returns:
        Object
        example:
            current_account = request['current_account']

    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method == 'POST':

                auth = Auth(request.headers.get('Authorization', None), permission)

                if auth.status():
                    print('request: ',request.json)
                    request.json['current_account'] = auth.account
                    return func(request, *args, **kwargs )

                else:
                    c,m,d = auth.errormsg()
                    return ReturnRequest(c,m,d)

            else:
                return ReturnRequest(405,'请求方法不正确',{})
        return wrapper
    return decorator

class Auth:
    """用户Token认证.

    使用前需要设置Auth内__init__下的用户表管理表的指向
    Adminclass = 管理员表类
    Userclass = 用户表类

    Args:
        permission:
            判断用户是什么类型用户并查找用户Token是否正确.
            如果是1 查询管理员表 2查询用户表

        token:
            用户请求的Token

    """
    def __init__(self, token, permission):

        # 设置类对象
        Adminclass = AccountAdmin
        Userclass = AccountUser

        if permission == 1:
            self.account = Adminclass.query.filter(Adminclass.token == token).first()

        elif permission == 2:
            self.account = Userclass.query.filter(Userclass.token == token).first()
        
        else:
            print('注意！[Middleware]@TOKEN: 未设置可访问的用户权限')

        self.token = token
        self.ret_data = {}
        self.ret_cnmsg = ''
        self.ret_code = BaseConfig.ERRORTOKEN

    def status(self):
        """获得Token认证结果
        创建auth = Auth()对象后
        auth.status()会返回用户是否通过验证 False验证失败，True验证成功
        """
        if not self.token:
            self.ret_cnmsg = '10086:1 - 非法请求 Token已失效或不正确, 请重新登录'
            self.ret_code = BaseConfig.ERRORTOKEN
            return False

        if not self.account:
            self.ret_cnmsg = '10086:2 - Token已失效或不正确, 请重新登录'
            self.ret_code = BaseConfig.ERRORTOKEN
            return False

        return True

    def account(self):
        """返回用户对象"""
        return self.account

    def errormsg(self):
        """返回异常
        self.ret_code, self.ret_cnmsg, self.ret_data
        
        错误码，错误消息，None
        """
        return self.ret_code, self.ret_cnmsg, self.ret_data
