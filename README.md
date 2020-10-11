# Flask-Cli

自己用的Flask 脚手架 注释[参照Google Python编写规范](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#comments)


## 结构介绍
``` sh
[项目基于工厂模式搭建]

# 内置的现成模块 可直接用
    Models.py   数据库类
    Email.py    邮件发送模块
    upload      多用上传模块

# 项目文件和结构说明
    |-manage.py
    |-requirements.txt
    |-app
        |-upload            文件上传模块
        |-__init__.py       构建工厂
        |-Blueprint.py      蓝图注册
        |-Config.py         配置文件
        |-Email.py          邮件发送模块
        |-Errorhandler.py   错误请求配置
        |-Extensions.py     引入依赖注册
        |-Middleware.py     中间件
        |-Models.py         数据库类
        |-Startprint.py     启动打印
        |-Tool.py           小工具
        |-RAM.py            项目运行时储存的共享参数
    |-env
    |-ini

# 使用依赖
    Blueprint
    Flask
    Flask-Caching   
    Flask-Cors      
    Flask-Docs      
    Flask-Mail      
    Flask-Migrate   
    Flask-RESTful   
    Flask-Script    
    Flask-SQLAlchemy
    mysqlclient
```

## Production
``` sh
# 部署路径
/home/{用户目录：默认ubuntu }/Service/{项目}/Api # Api是配置文件默认的项目文件夹名

# 部署要求 Supervisor Uwsgi Nginx Mysql Redis Python

# 配置文件路径
|-Api
    |-app
    |-env
    |-ini
        |-uwsgi.ini
        |-supervisort   # 配置完成后把 supervisor 文件放置 /etc/supervisor/conf.d/
        |-nginx.conf    # 配置完成后把 nginx 文件放置 /etc/nginx/sites-enabled/
```

## Config
``` python
app/Config.py

DevelopmentConfig
ProductionConfig
```

## Development Setup

``` sh
# start project
python manager.py runserver
```

## Migrations

``` sh
# create migrations
python manage.py db init

# upchange
python manage.py db migrate

# updatesql
python manage.py db upgrade
```

## Pipenv Packages

``` sh
# install virtualenv
pip install virtualenv

# create env
virtualenv env

# use env
Liunx: source env/bin/activate
Windows: env/scripts/activate

# install pip lib in env
(env) pip install -r requirements.txt
```