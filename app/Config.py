# coding: utf-8
 
'''
    # Flask 配置文件

    使用参数
        from flask import current_app
        config = current_app.config
        SITE_DOMAIN = config.get('SITE_DOMAIN')

    [SQLALCHEMY_DATABASE_URI]
        数据库地址
        SQLALCHEMY_DATABASE_URI = "mysql://root: 密码 @ IP : 端口 / 数据库名 ?charset=utf8mb4"

    [Flask-Email]
        MAIL_SERVER = ''
        MAIL_PORT = 25
        MAIL_USE_TLS = True
        MAIL_USERNAME = ''
        MAIL_PASSWORD = ''
'''

import logging

class BaseConfig:
    """
        基本配置类
    """

    RUNSERVER_IP = '127.0.0.1'
    RUNSERVER_PORT = 8000

    # Token失效时默认返回
    ERRORTOKEN = 10086

    # 跨域密钥
    SECRET_KEY = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

    # Flask-Docs参数(API_DOC_MEMBER:蓝图名, RESTFUL_API_DOC_EXCLUDE:排除的api名, APIDOC_VERSION: api文档版本, APIDOC_TITLE: api文档标题)
    APIDOC_TITLE = "Flask-CLi"
    APIDOC_VERSION = "0.0"

    # API_DOC_MEMBER是放置要生成API文档的蓝图名 已经在创建蓝图的时候自动生成了 不需要在手动写了
    API_DOC_MEMBER = []

    # 不想生成API文档的蓝图模块可以写在RESTFUL_API_DOC_EXCLUDE里面
    RESTFUL_API_DOC_EXCLUDE = []

    UPLOADFILE_CONFIG = {
        'userhead': '/head/',
    }

    LOG_LEVEL = logging.DEBUG

    LOG_PATH = 'logs/logs'

class DevelopmentConfig(BaseConfig):
    """
        开发环境配置
    """
    
    PREFIX_TITLE = ''

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://CyTkhMdycB:Xv7cT9rT2G@remotemysql.com:3306/CyTkhMdycB?charset=utf8mb4"

    # 文件加载地址
    STATIC_LOADPATH = "http://127.0.0.1:8000/static"

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    LOG_LEVEL = logging.DEBUG


class ProductionConfig(BaseConfig):
    """
        线上环境配置
    """
    
    PREFIX_TITLE = '/api'

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ""

    # 文件加载地址
    STATIC_LOADPATH = "http://192.168.0.1/static"

    LOG_LEVEL = logging.WARNING

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}