from re import I
from . import BaseModel, BaseModelAuth
from app.Extensions import db
from flask_bcrypt import generate_password_hash, check_password_hash
from app.Config import config
from app.RAM import AppRAM

class AccountInfo(object):
    """用户表模型基类
    为用户表和管理表继承相同字段和公共方法
        head,
        account,
        email,
        phone,
        password,
        username,
    """

    account = db.Column(db.Text)                        # 账户          a-z0-9A-z
    email = db.Column(db.Text)                          # 用户邮箱
    phone = db.Column(db.Integer)                       # 用户手机
    head = db.Column(db.Text)                           # 头像
    password = db.Column(db.Text)                       # 密码
    username = db.Column(db.String(255))                # 用户名

    def _set_new_password(self, plaintext):
        """设置新的密码"""
        newpassword = generate_password_hash(plaintext)
        self.password = newpassword

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

    def _AccountInfo_Base(self):
        """返回模型基类参数"""
        return dict(
            username = self.username,
            head = self.userhead
        )


class AccountAdmin(BaseModel, AccountInfo, BaseModelAuth, db.Model):
    """管理员表"""

    __tablename__ = 'account_admin'
    
    remarks = db.Column(db.String(255))                 # 账户备注
    jurisdiction = db.Column(db.Integer, default=1)     # 管理员角色        1 高级管理员 2 一般管理员

    def toDict(self):
        return dict(
            remarks=self.remarks,
            jurisdiction=self.jurisdiction,
            **self._base(),
            **self._BaseModelAuth_Base(),
            **self._AccountInfo_Base()
        )

    def createadmin(self, username, email, password):
        """新增管理员(username: 用户名，email: 登录邮箱，password: 密码)"""
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self._add()
        self._commit()
        return self


class AccountUser(BaseModel, AccountInfo, BaseModelAuth, db.Model):
    """用户表"""

    __tablename__ = 'account_user'

    introduce = db.Column(db.Text)                      # 个人介绍

    def toDict(self):
        return dict(
            introduce=self.introduce,
            **self._base(),
            **self._BaseModelAuth_Base(),
            **self._AccountInfo_Base()
        )