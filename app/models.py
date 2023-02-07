from datetime import datetime

from sqlalchemy import DateTime

from app.app import db


class Users(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    username = db.Column(db.String(1000), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    register_date = db.Column(DateTime, default=datetime.now())
