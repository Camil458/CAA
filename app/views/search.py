from flask import Blueprint, render_template, request

from app.models import Offer, Category, Car, Brand, Model
from app.views.forms import SearchForm

bp = Blueprint('search', __name__)


@bp.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        offers = Offer.query.all()

        category = form.category.data
        brand = form.brand.data
        model = form.model.data
        from_year = form.from_year.data
        to_year = form.to_year.data
        mileage = form.mileage.data
        transmission = form.transmission.data
        accident = form.accident.data

        _offers = []
        for offer in offers:
            verified = True

            _car = Car.query.filter_by(id=offer.car_id).first()
            _brand = Brand.query.filter_by(bid=_car.bid).first()
            _model = Model.query.filter_by(mid=_car.mid).first()

            if category:
                _category = Category.query.filter_by(name=category).first()
                if _category.cid != _car.cid:
                    verified = False
            if brand:
                if brand != _brand.name:
                    verified = False
            if model:
                if model != _model.name:
                    verified = False
            if from_year:
                if from_year > _car.year:
                    verified = False
            if to_year:
                if to_year < _car.year:
                    verified = False
            if mileage:
                if mileage < _car.mileage:
                    verified = False
            if transmission:
                if transmission != _car.transmission:
                    verified = False
            if accident:
                if accident != _car.accident:
                    verified = False

            if verified:
                _offer = {
                    "id": offer.id,
                    "title": offer.title,
                    "price": offer.price,
                    "brand": _brand.name,
                    "model": _model.name,
                    "year": _car.year
                }
                _offers.append(_offer)

        return render_template('index.html', offers=_offers)

    return render_template('search.html', form=form)
