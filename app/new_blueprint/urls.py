from app.new_blueprint import new_blueprint, views
from app.Common import ReturnRequest
from app.Middleware import NORMAL, TOKEN

@new_blueprint.route('/demo-api', methods=["POST"])
@TOKEN(2)
def Demo_Api(request):
    """Demo"""
    return ReturnRequest(views.Demo_Api(request.json))