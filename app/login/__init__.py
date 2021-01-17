from flask import Blueprint
login = Blueprint('login', __name__)
from ..login import urls