# coding: utf-8
from datetime import datetime
from app.Extensions import db

class BaseModel(object):
    """数据库表基类
        补充id， create_time， update_time

        数据库事务方法:
            _delete()
            _add()
            _commit()
    """
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)                          # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)   # 记录的更新时间

    def _delete(self):
        """delete方法"""
        db.session.delete(self)

    def _add(self,data=None):
        """add()方法"""
        db.session.add(self)

    def _commit(self,data=None):
        """带事务提交成功
            返回200，失败返回400
            :data 附加返回数据
        """
        try:
            db.session.commit()
            if data:
                return 200, "成功", dict({"id":self.id},**data)
            return 200, "成功", {"id":self.id}

        except Exception as e:
            print("事务异常>",e)
            db.session.rollback()
            return 400, "内部出错", {}

    def _base(self):
        """返回模型基类参数"""
        return dict(
            id = self.id,
            create_time = datetime.strftime(self.create_time, "%Y-%m-%d %H:%M:%S"),
            update_time = datetime.strftime(self.update_time, "%Y-%m-%d %H:%M:%S")
        )


class BaseModelAuth(object):
    """认证基础表
        token, status"""
    
    token = db.Column(db.Text)
    status = db.Column(db.Integer, default=0)   # 用户状态          0正常 1禁止登录

    def _set_token(self):
        """设置新的Token"""
        from app.Tool import GenerateToken
        self.token = GenerateToken(str(self.account))
        return True

    def _clear_token(self):
        """清除Token"""
        self.token = None
        return True

    def _BaseModelAuth_Base(self):
        return dict(
            status = self.status
        )