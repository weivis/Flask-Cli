# coding: utf-8
import os
from app import create_app
from app.Extensions import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Server, Command, Option
from app.Models import DemoTable, AccountAdmin, AccountUser
from app.Config import BaseConfig, config

# 设置运行模式 production, development
RUN_CONFIG = 'development'

app = create_app(RUN_CONFIG)
manager = Manager(app)
migrate = Migrate(app, db)

class CreateAdmin(Command):
    """Create new admin account"""

    option_list = (
        Option('-u', '--username', dest='username', default=None),
        Option('-a', '--account', dest='account', default=None),
        Option('-p', '--password', dest='password', default=None)
    )

    def run(self, username, account, password):
        if not all([username, account, password]):
            raise AttributeError("参数有误, 创建管理员方法必须输入管理员用户名,登录账户,密码, -u -a -p")

        add = AccountAdmin().createadmin(username, account, password)
        print("创建新管理员" + " < " + add.username," ID:", add.id, " > " + "成功")
        print("账户:",add.account)
        print("密码:",add.password)
        
manager.add_command("db", MigrateCommand)
manager.add_command("runserver", Server(port=BaseConfig.RUNSERVER_PORT, host=BaseConfig.RUNSERVER_IP, use_debugger=config[RUN_CONFIG].DEBUG))
manager.add_command("createadmin", CreateAdmin())

if __name__ == '__main__':
    manager.run()