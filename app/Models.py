# coding: utf-8
"""
    建议:
        尽量不要用0做默认状态 处理不好会和None冲突

    规范说明:
        每个表必须存在更新时间和创建时间 可选参数[ index=True ] 设为索引
        update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
        create_time = db.Column(db.DateTime, default=datetime.now)

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

        范文:
	        def toDict(self, filter=[]):
	            """
	                filter, [], 可选参数
	                    :无
	            """
	            json = {
	                'id': id,
	            }
	            return json
"""

from datetime import datetime
from app.Extensions import db

class DomeTable(db.Model):
    
    __tablename__ = 'dometable'
    id = db.Column(db.Integer, primary_key=True)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def toDict(self, filter=[]):
        """
            filter, [], 可选参数
                :无
        """
        json = {
            'id': id,
        }
        return json