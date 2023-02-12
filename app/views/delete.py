from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user

from app.app import db
from app.models import Offer, Car, Engine

bp = Blueprint('delete', __name__)


@bp.route('/delete/<string:offer_id>')
@login_required
def delete(offer_id: int):
    offer_to_delete = Offer.query.get_or_404(offer_id)
    if offer_to_delete.user_id == int(current_user.get_id()):
        car_to_delete = Car.query.get_or_404(offer_to_delete.car_id)
        engine_to_delete = Engine.query.get_or_404(car_to_delete.eid)

        try:
            db.session.delete(offer_to_delete)
            db.session.commit()
            db.session.delete(car_to_delete)
            db.session.commit()
            db.session.delete(engine_to_delete)
            db.session.commit()
            flash('Offer deleted successfully', 'success')
        except:
            flash("Whoops! There was a problem deleting offer, try again later", 'danger')

    return redirect(url_for('index.index'))
