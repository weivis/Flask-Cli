from app.Models import AccountAdmin

def adminSignin(request):
    account = request.get("account",None)
    password = request.get("password",None)

    obj = AccountAdmin.query.filter(AccountAdmin.account == account).first()
    if obj and obj._is_correct_password(password):

        if obj.status != 0:
            return 400, "该账户存在异常 已被禁止登录", {}

        obj._set_token()
        return 200, "", obj.toDict()
        
    return 400, "账户密码不正确", {}