from app.user import user, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

@user.route('/get', methods=["POST"])
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

@user.route('/put', methods=["POST"])
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

@user.route('/', methods=["POST"])
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
    
    return ReturnRequest(views.UserQuery(request.json))
