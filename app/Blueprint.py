# coding: utf-8
"""
    引入蓝图模块
"""
from app.demo import demo
from app.upload import upload
from app.user import user
from app.Config import BaseConfig


"""
    配置蓝图映
        ()后面必须加, 否则无法正常启动
"""
DEFAULT_BLUEPRINT = (
    (demo, '/demo'),
    (upload, '/upload'),
    (user, '/user')
)

def config_blueprint(app):
    """
        读取蓝图配置
    """

    API_DOC_MEMBER = []

    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)

        # 自动设置Flas-Docs的API_DOC_MEMBER参数
        blueprintName = str(blueprint.name)
        if blueprintName not in BaseConfig.RESTFUL_API_DOC_EXCLUDE:

            # 把蓝图模块名储存起来更新到配置文件
            API_DOC_MEMBER.append(blueprintName)

    app.config['API_DOC_MEMBER'] = BaseConfig.API_DOC_MEMBER + API_DOC_MEMBER