from flask import Blueprint, render_template

bp = Blueprint('login', __name__)


@bp.route('/login')
def index():
    return render_template('login.html')