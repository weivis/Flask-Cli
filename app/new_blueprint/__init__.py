from flask import Blueprint
new_blueprint = Blueprint('new_blueprint', __name__)
from ..new_blueprint import urls