# coding: utf-8
from flask import Flask
from app.Blueprint import config_blueprint
from app.Extensions import config_extensions
from app.Errorhandler import config_errorhandler
from app.Startprint import config_startprint
from app.Config import config
from app.RAM import AppRAM

def create_app(runConfig='default'):
    """构建入口 create_app()

    :param runConfig: 运行配置文件 默认default, 可选'development', 'production'

    :param static_folder: 参数用于设定当前静态文件路径 如果需要返回上一级路径可以使用以下代码
                          import os / os.path.abspath("../static") 默认为'static'

    :config_extensions 注册扩展初始化init
    :config_blueprint 载入蓝图
    :config_errorhandler 载入异常请求处理
    :config_startprint 载入启动打印
    """

    app = Flask(__name__, static_folder='static')
    
    app.config.from_object(config[runConfig])

    config_extensions(app)

    config_blueprint(app)

    AppRAM.runConfig = runConfig

    config_errorhandler(app)

    config_startprint(app)

    return app