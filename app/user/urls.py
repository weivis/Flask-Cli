from app.user import user, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

@user.route('/my/account/put', methods=["POST"])
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