# coding: utf-8

from flask import Flask
from app.Blueprint import config_blueprint
from app.Extensions import config_extensions
from app.Errorhandler import config_errorhandler
from app.Startprint import config_startprint, config_overstart
from app.Config import config
from app.RAM import AppRAM

def create_app(runConfig='default'):
    """构建入口 create_app()

    :param runConfig: 运行配置文件 默认default, 可选'development', 'production'

    :config_extensions 注册扩展初始化init
    :config_blueprint 载入蓝图
    :config_errorhandler 载入异常请求处理
    :config_startprint 载入启动打印
    """

    app = Flask(__name__, static_folder='static')
    
    AppRAM.runConfig = runConfig

    app.config.from_object(config[runConfig])

    config_startprint(app, runConfig)

    config_extensions(app)

    config_blueprint(app, runConfig)

    config_errorhandler(app)

    config_overstart()

    return app