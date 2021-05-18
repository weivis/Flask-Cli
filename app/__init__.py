# coding: utf-8

from flask import Flask
from app.Blueprint import config_blueprint
from app.Extensions import config_extensions
from app.Errorhandler import config_errorhandler
from app.Startprint import config_startprint, config_overstart
from app.Logs import config_runninglog
from app.Config import config
import logging

def create_app(ENV='default'):
    """构建入口 create_app()

    :param runConfig: 运行配置文件 默认default, 可选'development', 'production'

    :config_extensions 注册扩展初始化init
    :config_blueprint 载入蓝图
    :config_errorhandler 载入异常请求处理
    :config_startprint 载入启动打印
    """

    app = Flask(__name__, static_folder='static')
    
    app.config.from_object(config[ENV])

    config_runninglog(ENV)

    config_startprint(app, ENV)

    config_extensions(app)

    config_blueprint(app, ENV)

    config_errorhandler(app)

    config_overstart()

    logging.debug('构建完成 > 测试日志打印')

    @app.route("/")
    def index():
        # print(LOAD_PATH)
        return ""
    
    return app
