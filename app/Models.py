# coding: utf-8
"""
	建议:
		尽量不要用0做默认状态 处理不好会和None冲突

    规范说明:
		每个表必须存在更新时间和创建时间 可选参数[ index=True ] 设为索引
		update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
		create_time = db.Column(db.DateTime, default=datetime.now)
		注: 建议直接继承基类 BaseModel

    基础Sql常用类型提供:
        参数说明[primary_key=True(设置字段内容不可重复), default(字段默认值)]
        db.Column(db.Integer, default=0)
        db.Column(db.Text)
        db.Column(db.String(255))
        db.Column(db.Date)
        db.Column(db.Boolean, default=False)
    
    常用参数序列化处理:
        datetime.strftime(self.字段名, "%Y-%m-%d %H:%M:%S")

    可选字段:
        软删除状态
        is_delete = db.Column(db.Boolean, default=False)

    toDict(self)使用方法:
        filter 默认下为空 '[]' 可以配合filter增加返回条件 如:

        1.
        filter = ['id']
        if "id" in filter:
            json = dict(json,**{"id": self.id})

        2.
        filter = ['userinfo']
        if "userinfo" in filter:
            json = dict(json,**{"userinfo": 用户表.query.filter_by(id=self.用户id).first().getUserinfo() })

        使用范文:
            def toDict(self, filter=[]):

                json = {
                    'id': id,
                }
                return json

	事务:
		flush: 写数据库，但不提交，也就是事务未结束
		commit: 是先调用flush写数据库，然后提交，结束事务，并开始新的事务
		flush之后你才能在这个Session中看到效果，而commit之后你才能从其它Session中看到效果
		db.session.add(mapping)
    	db.session.flush()
		db.session.commit()
"""

from datetime import datetime
from app.Extensions import db
from flask_bcrypt import check_password_hash, generate_password_hash
import hashlib

class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间

    可以继承该基类给每个表加上create_time， update_time

    create_time:
            行创建时间

    update_time:
            每次该数据发送变化时会被更新

    """
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间

    def __repr__(self):
        return '[ repr ] Class: %s, ID: %r' % (self.__class__.__name__, self.id)


class ErrorLog(BaseModel, db.Model):
    """用于储存程序发生的错误到数据库"""

    __tablename__ = 'error_log'
    address = db.Column(db.String(255))
    error_content = db.Column(db.Text)
    level = db.Column(db.Integer, default=0)

    def __init__(self, address, error_content, level = 0):
        self.address = address
        self.error_content = error_content
        self.level = level
        self.update()

    def update(self):
        db.session.add(self)
        db.session.commit()


class DemoTable(BaseModel, db.Model):
    __tablename__ = 'demo_table'
    title = db.Column(db.String(255))
    content = db.Column(db.Text)

    def toDict(self):
        return dict(
            title=self.title,
            content=self.content
        )


class AccountAdmin(BaseModel, db.Model):

    __tablename__ = 'account_admin'
    token = db.Column(db.Text)
    account = db.Column(db.Text)
    username = db.Column(db.String(255))
    password = db.Column(db.Text)


    def createadmin(self, username, account, password):
        self.account = account
        self.username = username
        self.password = password
        self.update()
        return self


    def SetToken(self):
        """设置新的Token"""
        from app.Tool import GenerateToken
        self.token = GenerateToken(self.account)
        db.session.commit()
        return True


    def ClearToken(self):
        """清除Token"""
        self.token = None
        return True


    def is_correct_password(self, plaintext):
        """判断密码 正确返回True"""
        if check_password_hash(self.password, plaintext):
            return True

    def update(self):
        db.session.add(self)
        db.session.commit()


class AccountUser(BaseModel, db.Model):

    __tablename__ = 'account_user'
    token = db.Column(db.Text)
    email = db.Column(db.Text)
    head = db.Column(db.Text)
    introduce = db.Column(db.Text)
    username = db.Column(db.String(255))
    password = db.Column(db.Text)
    status = db.Column(db.Integer, default=0)

    def SetToken(self):
        """设置新的Token"""
        from app.Tool import GenerateToken
        self.token = GenerateToken(self.account)
        db.session.commit()
        return True


    def SetUserStatus(self, newstatus):
        """设置用户Status"""
        self.status = newstatus
        db.session.commit()


    def ClearToken(self):
        """清除Token"""
        self.token = None
        return True


    def is_correct_password(self, plaintext):
        """判断密码 正确返回True"""
        if check_password_hash(self.password, plaintext):
            return True