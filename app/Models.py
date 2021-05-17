# coding: utf-8
from datetime import datetime
from app.Extensions import db
from flask_bcrypt import check_password_hash, generate_password_hash
import hashlib
from app.RAM import AppRAM
from app.Config import config

"""
    Column:
        db.Column(db.Integer)
        db.Column(db.Text)
        db.Column(db.String(255))
        db.Column(LONGTEXT)             from sqlalchemy.dialects.mysql import LONGTEXT
        db.Column(db.DateTime)
        db.Column(db.Boolean, default=False)
"""
