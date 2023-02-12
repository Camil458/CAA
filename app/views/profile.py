from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models import User, Offer, Car, Brand, Model

bp = Blueprint('profile', __name__)


@bp.route('/profile')
@login_required
def profile():
    user = User.query.filter_by(id=current_user.get_id()).first()
    _user = {
        "name": user.name,
        "username": user.username,
        "email": user.email,
    }

    offers = Offer.query.all()

    _offers = []
    for offer in offers:
        if offer.user_id == int(current_user.get_id()):
            car = Car.query.filter_by().first()
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

    return render_template('profile.html', user=_user, offers=_offers)
