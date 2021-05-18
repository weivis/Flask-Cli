"""
    desc = 从大到小
"""

"""
    get
"""
from app.models.account import AccountUser
from app.Tool import _Paginate
def get(request):
    id = request.get("id", None)

    if id:
        obj = AccountUser.query.get(id)
        if not obj:
            return 400, "找不到内容", {}
    else:
        querypage = request.get('querypage',1)
        perpage = request.get('perpage',10)
        keyword = request.get('keyword', None)
        querys = AccountUser.query.filter()

        if keyword:
            querys = querys.filter_by(id.contains(keyword))

        querys = querys.order_by(AccountUser.create_time.desc())
        AccountUser.query.filter().first()
        total, result, pageCount, totalPages = _Paginate(querys, querypage, perpage)
        return 200, "", {
            "total":total,
            "result":[i.toDict() for i in result],
            "pageCount":pageCount,
            "totalPages":totalPages
        }

"""
    post
"""
from app.models.account import AccountUser
def post(request):
    email = request.get('email',None)

    if not email:
        return 400, "", {}

    add = AccountUser()
    add.email = email
    add._add()
    return add._commit()

"""
    put
"""
from app.models.account import AccountUser
def put(request):
    id = request.get("id", None)

    if not id:
        return 400, "id不能为空", {}

    obj = AccountUser.query.get(id)
    if not obj:
        return 400, "id或数据有误", {}

    # obj.xxx = xxx

    return obj._commit()

    
"""
    del
"""
from app.models.account import AccountUser
def del(request):
    id = request.get("id", None)

    if not id:
        return 400, "id不能为空", {}

    obj = AccountUser.query.get(id)
    if not obj:
        return 400, "id或数据有误", {}

    obj._delete()
    return obj._commit()