# coding: utf-8
from flask_caching import Cache
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from app.Config import BaseConfig
from flask_docs import ApiDoc

db = SQLAlchemy()
mail = Mail()
cache = Cache()

apidoc = ApiDoc()

def config_extensions(app):
    """
        初始化引入库:init_app
    """

    CORS(app, supports_credentials=True)

    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

    db.init_app(app)

    mail.init_app(app)

    apidoc.init_app(app, title=BaseConfig.APIDOC_TITLE, version=BaseConfig.APIDOC_VERSION)