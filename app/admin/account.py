from app.Models import AccountAdmin
from app.Tool import _Paginate
from app.Extensions import db

def AccountGet(request):
    current_account = request['current_account']
    return 200, "", current_account.toDict()

def AccountPut(request):

    current_account = request['current_account']

    head = request.get("head", None)
    username = request.get("username", None)

    if head:
        current_account.head = head
    
    if username:
        current_account.username = username
    
    try:
        current_account._update()
        return 200, "", {
            "userhead": current_account.userhead
        }

    except Exception as e:
        print(e)
        return 400, "出错", {}


def AccountList(request):
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


def AccountPost(request):
    from flask_bcrypt import generate_password_hash

    email = request.get('email',None)
    username = request.get('username',None)
    password = request.get('password',None)
    jurisdiction = request.get('jurisdiction',None)
    remarks = request.get('remarks',None)

    if not all([email, username, password, jurisdiction]):
        return 400, "信息填写不正确", {}

    add = AccountAdmin()
    add.account = email
    add.username = username
    add.password = generate_password_hash(password)
    add.jurisdiction = jurisdiction
    add.remarks = remarks
    add.status = 0
    
    try:
        add._update()
        return 200, "", {}

    except Exception as e:
        print(e)
        return 400, "出错", {}


def AccountInfoPut(request):
    id = request.get('id',None)
    sets = request.get('set',None)

    obj = AccountAdmin.query.get(id)
    if not obj:
        return 400, "账户不存在", {}

    if sets == 1:
        obj.changestatus()
        return 200, "", {}

    if sets == 2:
        db.session.delete(obj)
        db.session.commit()
        return 200, "", {}

    if sets == 3:
        from flask_bcrypt import generate_password_hash
        passwort = request.get('passwort',None)

        if not passwort:
            return 400, "密码不能为空", {}

        obj.passwort = generate_password_hash(passwort)
        obj._update()
        return 200, "修改成功", {}

    if sets == 4:
        obj.remarks = request.get('remarks',None)
        obj._update()
        return 200, "修改成功", {}

    if sets == 5:
        email = request.get('email',None)
        if not email:
            return 400, "不允许为空", {}
        obj.account = email
        obj._update()
        return 200, "修改成功", {}
    
