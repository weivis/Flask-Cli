# coding: utf-8
"""
    引入蓝图模块
"""
from app.demo import demo
from app.upload import upload
from app.user import user
from app.Config import BaseConfig
from app.account import account
from app.auth import auth

DEFAULT_BLUEPRINT = (
    (demo, '/demo'),
    (upload, '/upload'),
    (user, '/user'),
    (account, '/account'),
    (auth, '/auth')
)

def config_blueprint(app, runConfig):
    """
        读取蓝图配置

        :param runConfig, 运行模式, production

        (线上模式)所有api会增加 '/api' 代理, 非线上模式时无'/api'代理

    """

    API_DOC_MEMBER = []

    for blueprint, prefix in DEFAULT_BLUEPRINT:
        if runConfig == "production":
            app.register_blueprint(blueprint, url_prefix = '/api' + prefix)
        else:
            app.register_blueprint(blueprint, url_prefix = prefix)

        # 自动设置Flas-Docs的API_DOC_MEMBER参数
        blueprintName = str(blueprint.name)
        if blueprintName not in BaseConfig.RESTFUL_API_DOC_EXCLUDE:

            # 把蓝图模块名储存起来更新到配置文件
            API_DOC_MEMBER.append(blueprintName)

    app.config['API_DOC_MEMBER'] = BaseConfig.API_DOC_MEMBER + API_DOC_MEMBER