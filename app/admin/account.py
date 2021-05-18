from app.models.account import AccountAdmin
from app.Tool import _Paginate
from app.Extensions import db

def admin_account_get(request):
    current_account = request['current_account']
    return 200, "", current_account.toDict()

def admin_account_put(request):

    current_account = request['current_account']

    head = request.get("head", None)
    username = request.get("username", None)

    if head:
        current_account.head = head
    
    if username:
        current_account.username = username
    
    return current_account._commit(data=dict(use = current_account.userhead))


def admin_account_list(request):
    querypage = request.get('querypage',1)
    perpage = request.get('perpage',10)
    
    querys = AccountAdmin.query.filter()
    querys = querys.order_by(AccountAdmin.create_time.desc())

    total, result, pageCount, totalPages = _Paginate(querys, querypage, perpage)
    return 200, "", {
        "total":total,
        "result":[i.toDict() for i in result],
        "pageCount":pageCount,
        "totalPages":totalPages
    }


def admin_account_post(request):
    from flask_bcrypt import generate_password_hash

    email = request.get('email',None)
    username = request.get('username',None)
    password = request.get('password',None)
    jurisdiction = request.get('jurisdiction',None)
    remarks = request.get('remarks',None)

    if not all([email, username, password, jurisdiction]):
        return 400, "信息填写不正确", {}

    add = AccountAdmin()
    add.email = email
    add.username = username
    add.password = generate_password_hash(password)
    add.jurisdiction = jurisdiction
    add.remarks = remarks
    add.status = 0
    add._add()
    return add._commit()


def other_admin_account_put(request):
    id = request.get('id',None)
    sets = request.get('set',None)

    obj = AccountAdmin.query.get(id)
    if not obj:
        return 400, "账户不存在", {}

    if sets == 1:
        if obj.status == 0:
            obj.status = 1
        else:
            obj.status = 0
        obj.changestatus()
        return obj._commit()

    if sets == 2:
        obj._delete()
        return obj._commit()

    if sets == 3:
        from flask_bcrypt import generate_password_hash
        passwort = request.get('passwort',None)

        if not passwort:
            return 400, "密码不能为空", {}

        obj.passwort = generate_password_hash(passwort)
        obj._update()
        return obj._commit()

    if sets == 4:
        obj.remarks = request.get('remarks',None)
        obj._update()
        return obj._commit()

    if sets == 5:
        email = request.get('email',None)
        if not email:
            return 400, "不允许为空", {}
        obj.email = email
        return obj._commit()
    
