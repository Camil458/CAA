from flask import Blueprint

bp = Blueprint('register', __name__)


@bp.route('/register')
def index():
    return 'register'