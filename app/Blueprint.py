# coding: utf-8
"""
    引入蓝图模块
"""
from app.demo import demo
from app.upload import upload
from app.Config import BaseConfig, config
from app.admin import admin
from app.user import user

DEFAULT_BLUEPRINT = (
    (demo, '/demo'),
    (upload, '/upload'),
    (admin, '/admin'),
    (user, '/user')
)

def config_blueprint(app, ENV):
    """
        读取蓝图配置

        :param ENV, 运行模式, production

        配置url_prefix的方法:
            在 Config.py内 PREFIX_TITLE属性 根据ENV自动选择

    """

    API_DOC_MEMBER = []

    for blueprint, prefix in DEFAULT_BLUEPRINT:
        if ENV == "production":
            app.register_blueprint(blueprint, url_prefix = config[ENV].PREFIX_TITLE + prefix)
        else:
            app.register_blueprint(blueprint, url_prefix = prefix)

        # 自动设置Flas-Docs的API_DOC_MEMBER参数
        blueprintName = str(blueprint.name)
        if blueprintName not in BaseConfig.RESTFUL_API_DOC_EXCLUDE:

            # 把蓝图模块名储存起来更新到配置文件
            API_DOC_MEMBER.append(blueprintName)

    app.config['API_DOC_MEMBER'] = BaseConfig.API_DOC_MEMBER + API_DOC_MEMBER