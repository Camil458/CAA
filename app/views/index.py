from flask import Blueprint, render_template
from app.models import Offer, Car, Brand, Model

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    offers = Offer.query.all()

    _offers = []
    for offer in offers:

        car = Car.query.filter_by(id=offer.car_id).first()
        brand = Brand.query.filter_by(bid=car.bid).first()
        model = Model.query.filter_by(mid=car.mid).first()

        _offer = {
            "id": offer.id,
            "title": offer.title,
            "price": offer.price,
            "brand": brand.name,
            "model": model.name,
            "year": car.year
        }
        _offers.append(_offer)

    return render_template('index.html', offers=_offers)
