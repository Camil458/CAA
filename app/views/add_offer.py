from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from app.views.forms import AddForm
from app.models import *

bp = Blueprint('add_offer', __name__)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_offer():
    form = AddForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        price = form.price.data

        brand = form.brand.data
        model = form.model.data
        category = form.category.data
        vin = form.vin.data
        year = form.year.data
        mileage = form.mileage.data
        transmission = form.transmission.data
        num_of_seats = form.num_of_seats.data
        color = form.color.data
        accident = form.accident.data
        country = form.country.data

        engine_capacity = form.engine_capacity.data
        engine_power = form.engine_power.data
        engine_fuel = form.engine_fuel.data

        desc = form.desc.data

        bid = create_brand(brand)
        mid = create_model(model, bid)
        cid = create_category(category)
        eid = create_engine(engine_capacity, engine_power, engine_fuel)

        user_id = current_user.get_id()

        car_id = create_car(bid, mid, cid, vin, year, mileage, eid, transmission, num_of_seats, color,
                            accident, country, desc)

        # add new offer to database
        car_offer = Offer(title=title, price=price, car_id=car_id, user_id=user_id)
        db.session.add(car_offer)
        db.session.commit()

        return redirect(url_for('index.index'))

    return render_template('add_offer.html', form=form)


def create_brand(brand_name):
    brand = Brand.query.filter_by(name=brand_name).first()

    if brand:
        return brand.bid
    else:
        # add new brand to database
        new_brand = Brand(name=brand_name)

        db.session.add(new_brand)
        db.session.commit()

        return new_brand.bid


def create_model(model_name, bid):
    model = Model.query.filter_by(name=model_name).first()

    if model:
        return model.mid
    else:
        # add new model to database
        new_model = Model(name=model_name, bid=bid)

        db.session.add(new_model)
        db.session.commit()

        return new_model.mid


def create_category(category_name):
    category = Category.query.filter_by(name=category_name).first()

    if category:
        return category.cid
    else:
        # add new category to database
        new_category = Category(name=category_name)

        db.session.add(new_category)
        db.session.commit()

        return new_category.cid


def create_engine(capacity, power, fuel):
    # add new engine
    new_engine = Engine(capacity=capacity, power=power, fuel=fuel)

    db.session.add(new_engine)
    db.session.commit()

    return new_engine.eid


def create_car(bid, mid, cid, vin, year, mileage, eid, transmission, num_of_seats, color, accident, country,
               desc):
    # add new car
    new_car = Car(bid=bid, mid=mid, cid=cid, vin=vin, year=year, mileage=mileage, eid=eid,
                  transmission=transmission, num_of_seats=num_of_seats, color=color, accident=accident,
                  country=country, desc=desc)
    db.session.add(new_car)
    db.session.commit()

    return new_car.id
