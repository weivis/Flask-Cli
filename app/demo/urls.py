from app.demo import demo, views
from app.Common import ReturnRequest
from app.Middleware import POST, TOKEN
from app.Email import SeedEmail
from app.Tool import GenerateToken


@demo.route('/post', methods=["POST"])
@POST
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
@POST
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
@POST
def gentoken(request):
    """Token生成测试"""
    print(GenerateToken("111"))
    return ReturnRequest(views.test(request.json))


@demo.route('/gentoken-foraccount', methods=["POST"])
@POST
def gentoken_foraccount(request):
    """Token生成测试 给用户更新Token"""
    from app.Models import AccountAdmin
    user = AccountAdmin._get(9)
    print(user)
    print("oldtoken: ", user.token)
    user._set_token()
    print(user.toDict())
    return ReturnRequest(views.test(request.json))
