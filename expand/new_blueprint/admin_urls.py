from app.new_blueprint import new_blueprint, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

@new_blueprint.route('/admin-demo-api', methods=["POST"])
@TOKEN(2)
def admin_demo_api(request):
    """Demo"""
    return ReturnRequest(views.Demo_Api(request.json))