from app.admin import admin, account, login
from app.user import views as user
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

@admin.route('/account/get', methods=["POST"])
@TOKEN(1)
def AccountGet(request):
    """获取用户信息
    Returns:
        email: str, 登录邮箱
        username: str, 用户名
        token: str, token
        jurisdiction: int, 用户角色 1 管理员 2 一般用户
        remarks: str, 账户备注
        head: str, 头像
    """
    return ReturnRequest(account.AccountGet(request.json))

@admin.route('/account/put', methods=["POST"])
@TOKEN(1)
def AccountPut(request):
    """修改用户信息
    Args:
        head: str, 头像
        username: str, 用户名

    Returns:
        code:
            200     成功
            400     失败
        data:
            userhead
    """
    return ReturnRequest(account.AccountPut(request.json))

@admin.route('/account', methods=["POST"])
@TOKEN(1)
def Account(request):
    """获取全部账户
    Args:
        querys: 查询集  
        query_page: int 需要获取的页数  

    Returns:
        {
            "code": 200,
            "data": {
                "currentPage": 1,
                "result": [
                    {
                        "email": "weivi@outlook.com",
                        "head": "http://127.0.0.1:8080/static/head/20201118023841327.jpg",
                        "id": 1,
                        "remarks": null,
                        "token": "1",
                        "username": "WeiVi"
                    }
                ],
                "total": 1,
                "totalPages": 1
            },
            "msg": "成功"
        }
    """
    return ReturnRequest(account.AccountList(request.json))

@admin.route('/account/post', methods=["POST"])
@TOKEN(1)
def AccountPost(request):
    """创建新账户
    Args:
        email: str, 登录邮箱
        username: str, 用户名
        password: str, 密码
        jurisdiction: int, 用户角色 1 管理员 2 一般用户
        remarks: str, 账户备注

    Returns:
        200 成功
    """
    return ReturnRequest(account.AccountPost(request.json))

@admin.route('/account/put', methods=["POST"])
@TOKEN(1)
def AccountInfoPut(request):
    """管理账户
    Args:
        id: int, 账户ID
        set: int, 需更改功能
            1 = 禁止登录或解禁
            2 = 删除账户
            3 = 修改密码
            passwort: str, 新密码
            4 = 设置备注
            remarks: str, 备注
            5 = 修改账户
            email: str, 邮箱

    Returns:
        200 成功

    """
    return ReturnRequest(account.AccountInfoPut(request.json))

@admin.route('/user', methods=["POST"])
@TOKEN(1)
def UserQuery(request):
    """获取用户列表

    Args:
        querypage (int): 请求的页数 默认是1
        pagesize (int): 获取的条数 默认是10
        keyword (str): 搜索关键字

    Returns:
        total: 总条数
        result: 列表
        currentPage: 当前页面
        pageCount: 总分页数
    """
    
    return ReturnRequest(user.UserQuery(request.json))

@admin.route('/user/get', methods=["POST"])
@TOKEN(2)
def UserGet(request):
    """获取用户信息

    Args:
        id (int): 用户id

    Returns:
        str: email, 用户邮箱
        str: head, 用户头像
        str: username, 用户名
        int: status, 用户状态
    """
    return ReturnRequest(views.UserGet(request.json))

@admin.route('/user/put', methods=["POST"])
@TOKEN(2)
def UserPut(request):
    """修改用户信息

    Args:
        username (str): 用户名
        head (str) 用户头像

    Returns:
        200: 成功
        400: 失败
    """
    
    return ReturnRequest(views.UserPut(request.json))

@admin.route('/signin', methods=["POST"])
@NORMAL
def Signin(request):
    """管理员登录接口
    Args:
        account: str, 账户
        password: str, 密码
    Returns:
        jurisdiction: int, 用户身份, 1高级管理员 2一般管理员
        token: str, http头部token
        email: str, 登录邮箱
        head: str, 头像
        username: str, 用户名
        remarks: str, 备注名
        status: int, 用户状态, 0正常 1禁止登录
    """
    return ReturnRequest(login.adminSignin(request.json))