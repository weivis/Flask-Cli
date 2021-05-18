from app.user import user, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

# 用户管理 ---------------------------------------------------------------

@user.route('/admin/list', methods=["POST"])
@TOKEN(1)
def admin_user_list(request):
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
    
    return ReturnRequest(views.user_list(request.json))

@user.route('/admin/put', methods=["POST"])
@TOKEN(2)
def admin_user_put(request):
    """修改用户信息

    Args:
        username (str): 用户名
        head (str) 用户头像

    Returns:
        200: 成功
        400: 失败
    """
    
    return ReturnRequest(views.user_put(request.json))

# --------------------------------------------------------------------------

@user.route('/my_user/put', methods=["POST"])
@TOKEN(2)
def my_account_put(request):
    """修改用户自己的信息

    Args:
        username (str): 用户名
        head (str) 用户头像

    Returns:
        200: 成功
        400: 失败
    """
    
    return ReturnRequest(views.user_put(request.json))

@user.route('/user/get', methods=["POST"])
@TOKEN(2)
def account_get(request):
    """获取用户信息

    Args:
        id (int): 用户id

    Returns:
        str: email, 用户邮箱
        str: head, 用户头像
        str: username, 用户名
        int: status, 用户状态
    """
    return ReturnRequest(views.user_get(request.json))

