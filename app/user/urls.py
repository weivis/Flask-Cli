from app.user import user, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

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

