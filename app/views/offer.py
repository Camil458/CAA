from flask import Blueprint, render_template

from app.models import *

bp = Blueprint('offer', __name__)


@bp.route('/offer/<string:offer_id>', methods=['GET'])
def get_offer(offer_id: int):
    offer = Offer.query.filter_by(id=offer_id).first()
    car = Car.query.filter_by(id=offer.car_id).first()
    brand = Brand.query.filter_by(bid=car.bid).first()
    model = Model.query.filter_by(mid=car.mid).first()
    category = Category.query.filter_by(cid=car.mid).first()
    engine = Engine.query.filter_by(eid=car.eid).first()
    user = User.query.filter_by(id=offer.user_id).first()

    _offer = {
        "title": offer.title,
        "price": offer.price,
        "category": category.name,
        "brand": brand.name,
        "model": model.name,
        "vin": car.vin,
        "year": car.year,
        "mileage": car.mileage,
        "engine_capacity": engine.capacity,
        "engine_power": engine.power,
        "engine_fuel": engine.fuel,
        "transmission": car.transmission,
        "num_of_seats": car.num_of_seats,
        "color": car.color,
        "accident": car.accident,
        "country": car.country,
        "description": car.desc,
        "owner": user.email
    }

    return render_template('offer.html', offer=_offer)
