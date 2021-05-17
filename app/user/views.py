from app.models.account import AccountUser
from app.Tool import _Paginate

def user_get(request):
    userid = request.get("id", None)

    if not userid:
        return 400, "用户id不能为空", {}

    user = AccountUser.query.get(userid).first()

    if user:
        return 200, "", user.toDict()
    else:
        return 400, "用户不存在", {}

def user_put(request):
    current_account = request['current_account']

    username = request.get("username", None)
    head = request.get("head", None)

    if username:
        current_account.username = username

    if head:
        current_account.head = head

    return current_account._update()

def user_list(request):

    querypage = request.get('querypage', 1)
    pagesize = request.get('pagesize', 10)
    querys = AccountUser.query.filter()

    keyword = request.get("keyword", None)
    if keyword:
        querys = querys.filter(AccountUser.username.contains(keyword),AccountUser.email.contains(keyword))

    querys = querys.order_by(AccountUser.create_time.desc())
    total, result, currentPage, pageCount = _Paginate(
        querys, querypage, pagesize)

    return 200, "", {
        "total": total,
        "result": [i.toDict() for i in result],
        "currentPage": currentPage,
        "pageCount": pageCount
    }