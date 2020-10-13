from app.user import user, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

@user.route('/demo-api', methods=["POST"])
@TOKEN(2)
def Demo_Api(request):
    """Demo"""
    return ReturnRequest(views.Demo_Api(request.json))