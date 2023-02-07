from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user

bp = Blueprint('logout', __name__)


@login_required
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index.index'))
