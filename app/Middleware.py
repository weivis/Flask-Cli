#coding=utf-8
from functools import wraps
from flask import request
from app.Common import ReturnRequest
from app.models.account import AccountAdmin, AccountUser
from app.Config import BaseConfig


def NORMAL(func=None, method=None):
    """
    通用GET, POST请求, 不需要验证TOKEN
    
    Args:
        method: str, 该中间件默认支持GET, POST， PUT， 等多种方法。可以用method = GET or POST 锁定仅支持某一种类型
    """

    if not method:
        method = ['GET','POST','PUT']

    else:
        method = [method]

    @wraps(func)
    def wrapper(*args, **kwargs):

        if request.method in method:
            return func(request, *args, **kwargs)
        else:
            return ReturnRequest((405,'请求方法不对',''))
    return wrapper


def TOKEN(permission):
    """
    Token验证
    
    请求时头部['headers'] 需要携带 'Authorization' 参数名 并传入token

    Args:
        permission: int, 设置允许访问的请求token类型, 1管理员, 2一般用户

    Returns:
        Object

    Example:
        current_account = request['current_account']

    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method == 'POST':

                token = request.headers.get('Authorization', None)
                if not token:
                    return ReturnRequest((BaseConfig.ERRORTOKEN, "用户Token不正确或有误", {}))

                if permission == 1:
                    account = AccountAdmin.query.filter(AccountAdmin.token == token).first()

                elif permission == 2:
                    account = AccountUser.query.filter(AccountUser.token == token).first()
                
                else:
                    print('注意！[Middleware]@TOKEN: 未设置可访问的用户权限')

                if account:
                    print('request: ',request.json)
                    request.json['current_account'] = account
                    return func(request, *args, **kwargs )

                else:
                    return ReturnRequest((BaseConfig.ERRORTOKEN, "用户Token不正确或有误", {}))

            else:
                return ReturnRequest((405,'请求方法不正确',{}))
        return wrapper
    return decorator


def ISUSER():
    """
    是否用户
    
    请求时头部['headers'] 需要携带 'Authorization' 参数名 并传入token

    Returns:
        Object

    Example:
        current_account = request['current_account']

    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method == 'POST':

                token = request.headers.get('Authorization', None)
                if token:
                    account = AccountUser.query.filter(AccountUser.token == token).first()
                else:
                    account = None
                
                print('request: ',request.json)
                request.json['current_account'] = account
                return func(request, *args, **kwargs )
                
            else:
                return ReturnRequest((405,'请求方法不正确',{}))
        return wrapper
    return decorator