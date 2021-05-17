from app.admin import admin, account, login
from app.user import views as user
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

# 管理员 ---------------------------------------------------------------------

@admin.route('/account/get', methods=["POST"])
@TOKEN(1)
def admin_account_get(request):
    """获取当前登录访问的管理员信息
    Returns:
        email: str, 登录邮箱
        username: str, 用户名
        token: str, token
        jurisdiction: int, 用户角色 1 管理员 2 一般用户
        remarks: str, 账户备注
        head: str, 头像
    """
    return ReturnRequest(account.admin_account_get(request.json))

@admin.route('/account/put', methods=["POST"])
@TOKEN(1)
def admin_account_put(request):
    """修改当前登录访问的管理员信息
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
    return ReturnRequest(account.admin_account_put(request.json))

@admin.route('/account/list', methods=["POST"])
@TOKEN(1)
def admin_account_list(request):
    """获取全部管理员账户
    Args:
        querys: 查询集  
        query_page: int 需要获取的页数  

    Returns:
    """
    return ReturnRequest(account.admin_account_list(request.json))

@admin.route('/account/post', methods=["POST"])
@TOKEN(1)
def admin_account_post(request):
    """创建新管理员账户
    Args:
        email: str, 登录邮箱
        username: str, 用户名
        password: str, 密码
        jurisdiction: int, 用户角色 1 管理员 2 一般用户
        remarks: str, 账户备注

    Returns:
        200 成功
    """
    return ReturnRequest(account.admin_account_post(request.json))

# 修改其他管理员信息 ---------------------------------------------------

@admin.route('/other_account/put', methods=["POST"])
@TOKEN(1)
def other_admin_account_put(request):
    """修改其他管理员的账户信息
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
    return ReturnRequest(account.other_admin_account_put(request.json))

# 用户管理 ---------------------------------------------------------------

@admin.route('/user/list', methods=["POST"])
@TOKEN(1)
def user_list(request):
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
    
    return ReturnRequest(user.user_list(request.json))

@admin.route('/user/get', methods=["POST"])
@TOKEN(2)
def user_get(request):
    """获取用户信息

    Args:
        id (int): 用户id

    Returns:
        str: email, 用户邮箱
        str: head, 用户头像
        str: username, 用户名
        int: status, 用户状态
    """
    return ReturnRequest(user.user_get(request.json))

@admin.route('/user/put', methods=["POST"])
@TOKEN(2)
def user_put(request):
    """修改用户信息

    Args:
        username (str): 用户名
        head (str) 用户头像

    Returns:
        200: 成功
        400: 失败
    """
    
    return ReturnRequest(user.user_put(request.json))

# 管理员登录 ------------------------------------------------------------------------

@admin.route('/signin', methods=["POST"])
@NORMAL
def admin_signin(request):
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