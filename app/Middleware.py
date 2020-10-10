#coding=utf-8
from functools import wraps
from flask import request
from app.Common import ReturnRequest

from app.Models.db_Account import AccountAdmin, AccountUser

def POST(func=None):
    """通用Post请求"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            return func(request, *args, **kwargs)
        else:
            return ReturnRequest(405,'请求方法不对','')
    return wrapper

def Token(permission):
    """
    Token验证
    
    请求时头部['headers'] 需要携带 'Authorization' 参数名 并传入token

    :Param permission: int, 设置允许访问的请求token类型, 1管理员, 2一般用户

    :Returns :current_account = request['current_account']
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
    
    def __init__(self, token, permission):

        # 设置类对象
        Adminclass = AccountAdmin
        Userclass = AccountUser

        if permission == '1':
            self.account = Adminclass.query.filter(Adminclass.token == token).first()

        if permission == '2':
            self.account = Userclass.query.filter(Userclass.token == token).first()

        self.token = token
        self.ret_data = {}
        self.ret_cnmsg = ''
        self.ret_code = 10086
        if not permission:
            print('注意！@UserTokenAuthPost: 未设置可访问的用户权限')

    def status(self):
        if not self.token:
            self.ret_cnmsg = '10086:1 - 非法请求 Token已失效或不正确, 请重新登录'
            self.ret_code = 10086
            return False

        if not self.account:
            self.ret_cnmsg = '10086:2 - Token已失效或不正确, 请重新登录'
            self.ret_code = 10086
            return False

        return True

    def account(self):
        return self.account

    def errormsg(self):
        return self.ret_code, self.ret_cnmsg, self.ret_data
