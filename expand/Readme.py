"""
    desc = 从大到小
"""
from datetime import datetime
def returntime():
    create_time = datetime.now()
    datetime.strftime(create_time, "%Y-%m-%d %H:%M:%S")

"""
    更多数据字段类型
"""
from app.Extensions import db
from sqlalchemy.dialects.mysql import LONGTEXT
from datetime import datetime
def demo():
    db.Column(db.Integer, default=0)
    db.Column(db.Text)
    db.Column(db.String(255))
    db.Column(LONGTEXT)
    db.Column(db.DateTime)
    db.Column(db.Boolean, default=False)
    db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


"""
    多表事务
"""
from app.Extensions import db
import logging
def Atomic():
    try:
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        logging.debug(e)
        db.session.rollback()
        return 400, "内部出错", {}

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