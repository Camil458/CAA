from flask_login import UserMixin
from datetime import datetime

from sqlalchemy import DateTime

from app.app import db


class User(UserMixin, db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    register_date = db.Column(DateTime, default=datetime.now())


class Brand(db.Model):
    bid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)


class Model(db.Model):
    mid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    bid = db.Column(db.Integer, db.ForeignKey('brand.bid'))


class Category(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)


class Subcategory(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    cid = db.Column(db.Integer, db.ForeignKey('category.cid'))


class Engine(db.Model):
    eid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    capacity = db.Column(db.Integer)
    power = db.Column(db.Integer)
    fuel = db.Column(db.Integer)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.Integer, db.ForeignKey('brand.bid'))
    mid = db.Column(db.Integer, db.ForeignKey('model.mid'))
    cid = db.Column(db.Integer, db.ForeignKey('category.cid'))
    sid = db.Column(db.Integer, db.ForeignKey('subcategory.sid'))
    vin = db.Column(db.String(30), unique=True)
    reg = db.Column(db.String(30))
    year = db.Column(db.Integer)
    millage = db.Column(db.Integer)
    eid = db.Column(db.Integer, db.ForeignKey('engine.eid'))
    transmission = db.Column(db.Integer)
    num_of_seats = db.Column(db.Integer)
    color = db.Column(db.String(20))
    accident = db.Column(db.Integer)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    desc = db.Column(db.String(1000))
    country = db.Column(db.String(30))
