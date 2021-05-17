from app.demo import demo, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN
from app.Email import SeedEmail
from app.Tool import GenerateToken

from app.models.account import AccountAdmin

@demo.route('/', methods=["GET"])
@NORMAL
def TEST(request):
    """快速GET测试入口"""
    q = AccountAdmin.query.filter().all()
    print(request)

    user = AccountAdmin.query.get(9)
    print(user._is_correct_password('12345'))
    # user._set_new_password("123456")
    # user._clear_token()

    li = ""
    for i in q:
        li = li + "<li>" + str(i.toDict()) +"</li>"
    return "<h1>执行完成</h1> <ul>" + li + "</ul>"


@demo.route('/post', methods=["POST"])
@NORMAL
def Post_Middleware_Request_Test(request):
    """POST中间件测试"""
    return ReturnRequest(views.test(request.json))


@demo.route('/token/user', methods=["POST"])
@TOKEN(2)
def Token_Middleware_UserRequest_Test(request):
    """TOKEN中间件测试(一般用户)"""
    return ReturnRequest(views.test(request.json))


@demo.route('/token/admin', methods=["POST"])
@TOKEN(1)
def Token_Middleware_AdminRequest_Test(request):
    """TOKEN中间件测试(管理员)"""
    return ReturnRequest(views.test(request.json))


@demo.route('/seedemail', methods=["POST"])
@NORMAL
def Seed_Email_Test(request):
    """邮件发送测试"""
    SeedEmail(
        recipients=['442981412@qq.com'],
        email_title="测试",
        email_body="BODY",
        email_html="<h>测试</h>"
    )
    return ReturnRequest(views.test(request.json))


@demo.route('/gentoken', methods=["POST"])
@NORMAL
def gentoken(request):
    """Token生成测试"""
    print(GenerateToken("111"))
    return ReturnRequest(views.test(request.json))


@demo.route('/gentoken-foraccount', methods=["POST"])
@NORMAL
def gentoken_foraccount(request):
    """Token生成测试 给用户更新Token"""
    user = AccountAdmin.query.get(9)
    print(user)
    print("oldtoken: ", user.token)
    user._set_token()
    print(user.toDict())

    print("AAAAAAAAAAAAAAA",AccountAdmin.query.get(20))

    q = AccountAdmin.query.filter().all()

    print([i.toDict() for i in q])

    return ReturnRequest(views.test(request.json))