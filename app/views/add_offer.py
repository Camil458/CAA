from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

from app.views.forms import AddForm
from app.models import *

bp = Blueprint('add_offer', __name__)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_offer():
    form = AddForm(request.form)
    if request.method == 'POST' and form.validate():
        brand = form.brand.data
        model = form.model.data
        category = form.category.data
        subcategory = form.subcategory.data
        vin = form.vin.data
        reg = form.reg.data
        year = form.year.data
        mileage = form.mileage.data

        engine_name = form.engine_name.data
        engine_capacity = form.engine_capacity.data
        engine_power = form.engine_power.data
        engine_fuel = form.engine_fuel.data

        transmission = form.transmission.data
        num_of_seats = form.num_of_seats.data
        color = form.color.data
        accident = form.accident.data
        country = form.country.data
        desc = form.desc.data

        bid = create_brand(brand)
        mid = create_model(model, bid)
        cid = create_category(category)
        sid = create_subcategory(subcategory, cid)
        eid = create_engine(engine_name, engine_capacity, engine_power, engine_fuel)

        uid = current_user.get_id()

        # add new car offer to database
        car_offer = Car(bid=bid, mid=mid, cid=cid, sid=sid, vin=vin, reg=reg, year=year, mileage=mileage, eid=eid,
                        transmission=transmission, num_of_seats=num_of_seats, color=color, accident=accident, uid=uid,
                        desc=desc, country=country)
        db.session.add(car_offer)
        db.session.commit()

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


def create_subcategory(subcategory_name, cid):
    subcategory = Subcategory.query.filter_by(name=subcategory_name).first()

    if subcategory:
        return subcategory.sid
    else:
        # add new subcategory to database
        new_subcategory = Subcategory(name=subcategory_name, cid=cid)

        db.session.add(new_subcategory)
        db.session.commit()

        return new_subcategory.sid


def create_engine(name, capacity, power, fuel):
    # add new engine
    new_engine = Engine(name=name, capacity=capacity, power=power, fuel=fuel)

    db.session.add(new_engine)
    db.session.commit()

    return new_engine.eid
