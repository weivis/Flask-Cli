# coding: utf-8
import os
from app import create_app
from app.Extensions import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Server
from app.Models import DemoTable
from app.Config import BaseConfig, config

RUN_CONFIG = 'development'

app = create_app(RUN_CONFIG)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(
    port=BaseConfig.RUNSERVER_PORT,
    host=BaseConfig.RUNSERVER_IP,
    use_debugger=config[RUN_CONFIG].DEBUG
))

if __name__ == '__main__':
    manager.run()
