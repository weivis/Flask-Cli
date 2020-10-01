from flask import Blueprint
demo = Blueprint('demo', __name__)
from ..demo import urls