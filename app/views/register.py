from flask import Blueprint, render_template

bp = Blueprint('register', __name__)


@bp.route('/register')
def index():
    return render_template('register.html')
