from app.demo import demo, views
from app.Common import ReturnRequest
from app.Middleware import POST, TOKEN

# Post测试
@demo.route('/', methods=["POST"])
@POST
def test(request):
    """测试"""
    return ReturnRequest(views.test(request.json))

# Token测试
@demo.route('/token', methods=["POST"])
@TOKEN(2)
def tokentest(request):
    """测试"""
    return ReturnRequest(views.test(request.json))

# AdminToken测试
@demo.route('/admintoken', methods=["POST"])
@TOKEN(1)
def admintokentest(request):
    """测试"""
    return ReturnRequest(views.test(request.json))