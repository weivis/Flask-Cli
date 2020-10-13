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
    update_time = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间

    # def _get(self, id):
    #     """用id获取单条数据"""
    #     return self.query.filter_by(id=id).first()

    def _update(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '[ repr ] Class: %s, ID: %r' % (self.__class__.__name__, self.id)


class BaseModel_Account(object):
    """用户表模型基类

    为用户表和管理表继承相同字段和公共方法

    _set_token():
        设置token

    _get(id):
        根据id获取单个对象
        return id.first()

    update():
        提交数据库
        self.commit()

    _clear_token():
        重置token
        account.self.token = None

    _is_correct_password(plaintext):
        检验密码 正确返回True 错误返回None

    """
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间

    # @classmethod
    # def _get(cls, id):
    #     """用id获取单条数据"""
    #     return cls.query.filter_by(id=id).first()

    def _set_token(self):
        """设置新的Token"""
        from app.Tool import GenerateToken
        self.token = GenerateToken(str(self.account))
        db.session.commit()
        return True

    def _set_new_password(self, plaintext):
        newpassword = generate_password_hash(plaintext)
        self.password = newpassword
        self._update()

    def _is_correct_password(self, plaintext):
        """判断密码 正确返回True"""
        if check_password_hash(self.password, plaintext):
            return True

    def _update(self):
        """提交至数据库"""
        db.session.add(self)
        db.session.commit()

    def _clear_token(self):
        """清除Token"""
        self.token = None
        db.session.commit()
        return True

    def __repr__(self):
        return '[ repr ] Class: %s, ID: %r' % (self.__class__.__name__, self.id)


class AccountAdmin(BaseModel_Account, db.Model):
    """管理员表"""

    __tablename__ = 'account_admin'
    account = db.Column(db.Text)
    username = db.Column(db.String(255))
    password = db.Column(db.Text)

    def toDict(self):
        return dict(
            id=self.id,
            token=self.token,
            account=self.account,
            username=self.username,
            password=self.password
        )

    def createadmin(self, username, account, password):
        self.account = account
        self.username = username
        self.password = generate_password_hash(password)
        self._update()
        return self


class AccountUser(BaseModel, db.Model):
    """用户表"""

    __tablename__ = 'account_user'
    email = db.Column(db.Text)
    head = db.Column(db.Text)
    introduce = db.Column(db.Text)
    username = db.Column(db.String(255))
    password = db.Column(db.Text)
    status = db.Column(db.Integer, default=0)

    def SetUserStatus(self, newstatus):
        """设置用户Status"""
        self.status = newstatus
        db.session.commit()


class ErrorLog(BaseModel, db.Model):
    """用于储存程序发生的错误到数据库"""

    __tablename__ = 'error_log'
    address = db.Column(db.String(255))
    error_content = db.Column(db.Text)
    level = db.Column(db.Integer, default=0)

    def __init__(self, address, error_content, level=0):
        self.address = address
        self.error_content = error_content
        self.level = level
        self._update()

    def toDict(self):
        return dict(
            address = self.address,
            error_content = self.error_content,
            level = self.level
        )


class DemoTable(BaseModel, db.Model):
    __tablename__ = 'demo_table'
    title = db.Column(db.String(255))
    content = db.Column(db.Text)

    def toDict(self):
        return dict(
            title=self.title,
            content=self.content
        )
