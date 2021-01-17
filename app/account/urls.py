from app.account import account, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

@account.route('/info', methods=["POST"])
@TOKEN(1)
def UserInfo(request):
    """获取用户信息
    Returns:
        email: str, 登录邮箱
        username: str, 用户名
        token: str, token
        jurisdiction: int, 用户角色 1 管理员 2 一般用户
        remarks: str, 账户备注
        head: str, 头像
    """
    return ReturnRequest(views.UserInfo(request.json))

@account.route('/change/userinfo', methods=["POST"])
@TOKEN(1)
def ChangeInfo(request):
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
    return ReturnRequest(views.ChangeInfo(request.json))

@account.route('/allaccount', methods=["POST"])
@TOKEN(1)
def AllAccount(request):
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
    return ReturnRequest(views.AllAccount(request.json))

@account.route('/create', methods=["POST"])
@TOKEN(1)
def CreateAccount(request):
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
    return ReturnRequest(views.CreateAccount(request.json))

@account.route('/manage', methods=["POST"])
@TOKEN(1)
def Manage(request):
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
    return ReturnRequest(views.Manage(request.json))