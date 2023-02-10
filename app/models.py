from flask_login import UserMixin
from datetime import datetime

from sqlalchemy import DateTime

from app.app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
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


class Engine(db.Model):
    eid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    capacity = db.Column(db.Integer)
    power = db.Column(db.Integer)
    fuel = db.Column(db.String(20))


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.Integer, db.ForeignKey('brand.bid'))
    mid = db.Column(db.Integer, db.ForeignKey('model.mid'))
    cid = db.Column(db.Integer, db.ForeignKey('category.cid'))
    vin = db.Column(db.String(30))
    reg = db.Column(db.String(30))
    year = db.Column(db.Integer)
    mileage = db.Column(db.Integer)
    eid = db.Column(db.Integer, db.ForeignKey('engine.eid'))
    transmission = db.Column(db.String(30))
    num_of_seats = db.Column(db.Integer)
    color = db.Column(db.String(20))
    accident = db.Column(db.String(30))
    desc = db.Column(db.String(1000))
    country = db.Column(db.String(30))


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    price = db.Column(db.Integer)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
