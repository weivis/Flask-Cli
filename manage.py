# coding: utf-8
import os
from app import create_app
from app.Extensions import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Server
from app.Models import DemoTable

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db',MigrateCommand)
manager.add_command("runserver", Server())

if __name__ == '__main__':
    manager.run()