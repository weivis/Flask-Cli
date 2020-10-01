# coding: utf-8
"""
    引入蓝图模块
"""
from app.demo import demo

"""
    配置蓝图映
        ()后面必须加, 否则无法正常启动
"""
DEFAULT_BLUEPRINT = (
    (demo, '/demo'),
)

def config_blueprint(app):
    """
        读取蓝图配置
    """
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)