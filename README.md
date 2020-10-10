# Flask-Cli

自己用的Flask 脚手架 注释[参照Google Python编写规范](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#comments)


## 集成

    [基于工厂模式结构]

    Models.py 数据库类
    Email.py 邮件发送模块

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

## Config
``` python
app/Config.py

DevelopmentConfig
ProductionConfig
```

## Development Setup

``` sh
#start project
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
# install pip lib
pip install -r requirements.txt
```