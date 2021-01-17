from app.auth import auth, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

@auth.route('/admin/signin', methods=["POST"])
@NORMAL
def adminSignin(request):
    """管理员登录接口
    Args:
        account: str, 账户
        password: str, 密码
    Returns:
        jurisdiction: int, 用户身份, 1管理员 2一般用户
        token: str, http头部token
        email: str, 登录邮箱
        head: str, 头像
        username: str, 用户名
        remarks: str, 备注名
        status: int, 用户状态, 0正常 1禁止登录
    """
    return ReturnRequest(views.adminSignin(request.json))