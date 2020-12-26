# coding: utf-8
from datetime import datetime
from app.Extensions import db
from flask_bcrypt import check_password_hash, generate_password_hash
import hashlib

"""
    Column:
        db.Column(db.Integer)
        db.Column(db.Text)
        db.Column(db.String(255))
        db.Column(LONGTEXT)             from sqlalchemy.dialects.mysql import LONGTEXT
        db.Column(db.DateTime)
        db.Column(db.Boolean, default=False)
"""

class BaseModel(object):
    """数据表模型基类，为每个模型补充创建时间与更新时间
    可以继承该基类给每个表加上create_time， update_time

    """
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)                          # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)   # 记录的更新时间

    def _update(self):
        """带事务提交成功返回200，失败返回400"""
        try:
            db.session.add(self)
            db.session.commit()
            return 200, "成功", {"id":self.id}

        except Exception as e:
            print("事务异常>",e)
            db.session.rollback()
            return 400, "出错", {}

    def _base(self):
        """返回模型基类参数"""
        return dict(
            id = self.id,
            create_time = datetime.strftime(self.create_time, "%Y-%m-%d %H:%M:%S"),
            update_time = datetime.strftime(self.update_time, "%Y-%m-%d %H:%M:%S")
        )


class BaseModel_Account(object):
    """用户表模型基类
    为用户表和管理表继承相同字段和公共方法

    """
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text)                                                          # Token
    create_time = db.Column(db.DateTime, default=datetime.now)                          # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)   # 记录的更新时间

    def _set_token(self):
        """设置新的Token"""
        from app.Tool import GenerateToken
        self.token = GenerateToken(str(self.account))
        db.session.commit()
        return True

    def _clear_token(self):
        """清除Token"""
        self.token = None
        db.session.commit()
        return True

    def _set_new_password(self, plaintext):
        """设置新的密码"""
        newpassword = generate_password_hash(plaintext)
        self.password = newpassword
        self._update()

    def _is_correct_password(self, plaintext):
        """判断密码 正确返回True"""
        if check_password_hash(self.password, plaintext):
            return True

    @property
    def userhead(self):
        """用户头像"""
        path = config[AppRAM.runConfig].STATIC_LOADPATH + '/static/head/'
        if self.head:
            return path + self.head
        return path + 'default-userhead.jpg'

    def _base(self):
        """返回模型基类参数"""
        return dict(
            id = self.id,
            create_time = datetime.strftime(self.create_time, "%Y-%m-%d %H:%M:%S"),
            update_time = datetime.strftime(self.update_time, "%Y-%m-%d %H:%M:%S")
        )

    def _update(self):
        """带事务提交成功返回200，失败返回400"""
        try:
            db.session.add(self)
            db.session.commit()
            return 200, "成功", {"id":self.id}

        except Exception as e:
            print("事务异常>",e)
            db.session.rollback()
            return 400, "出错", {}


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class AccountAdmin(BaseModel_Account, db.Model):
    """管理员表"""

    __tablename__ = 'account_admin'
    head = db.Column(db.Text)
    account = db.Column(db.Text)
    username = db.Column(db.String(255))
    password = db.Column(db.Text)

    def toDict(self):
        return dict(
            token=self.token,
            account=self.account,
            username=self.username,
            **self._base()
        )

    def createadmin(self, username, account, password):
        """新增管理员"""
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
    username = db.Column(db.String(255))
    password = db.Column(db.Text)
    introduce = db.Column(db.Text)
    status = db.Column(db.Integer, default=0)

    def toDict(self):
        return dict(
            email=self.email,
            head=self.userhead,
            username=self.username,
            introduce=self.introduce,
            status=self.status,
            **self._base()
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
