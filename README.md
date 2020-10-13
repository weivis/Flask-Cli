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
            |-SeedEmail 邮件发送方法
        |-Errorhandler.py   错误请求配置
        |-Extensions.py     引入依赖注册
        |-Middleware.py     中间件
            |-Token 请求认证
            |-POST 普通请求
        |-Models.py         数据库类
            |-数据库基类
            |-用户表
            |-管理员表
            |-异常记录表
        |-Startprint.py     启动打印
        |-Tool.py           小工具
        |-RAM.py            项目运行时储存的共享参数
    |-env
    |-ini
    |-expand
        |-new_blueprint     蓝图模板 直接复制到app内修改蓝图注册名即可

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

## Start
``` sh
# start project
(env)python manager.py runserver

# 见到输出台打印以下内容表示启动成功
---------------------------------------------------------------------------------------------
启动时间: 2020-10-12 05:57:29.058991
Run in    :  < development > Config
Live Docs :  http://127.0.0.1:80/docs/api/
```

## Create NewAdmin
``` sh
# create manager
(env)python manager.py

    @ createadmin
    -u  用户名
    -a  账户
    -p  密码

    # python manage.py createadmin -u Administrator -a admin -p 123456 

# 看到打印台输出以下内容表示创建成功

创建新管理员 < Administrator  ID: 1  > 成功
账户: admin
密码: 123456

```

## BaseModel
``` sh
# Models内提供两个基础模型基类

    BaseModel
        id
        create_time
        update_time

        _update()

    BaseModel_Account
        id
        token
        create_time
        update_time

        _set_token()
        _is_correct_password()
        _update()
        _clear_token()

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

## 统一返回说明

    requestStatus: 200
        code    业务码
        data    数据
        msg     消息
    
    requestStatus: !200
        请求异常 不会返回数据

    先判断status 后判断code