from flask import Blueprint

bp = Blueprint('login', __name__)


@bp.route('/login')
def index():
    return 'login'