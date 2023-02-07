from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash

from app.views.forms import LoginForm
from flask_login import login_user

from app.models import User

bp = Blueprint('login', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        # if this returns a user, then the email already exists in database
        user = User.query.filter_by(username=username).first()

        if user:
            if not check_password_hash(user.password, password):
                error = "Incorrect password"
                return render_template('login.html', form=form, error=error)
            else:
                login_user(user)
                return redirect(url_for('index.index'))
        else:
            error = "There is no user: " + str(username)
            return render_template('login.html', form=form, error=error)

    return render_template('login.html', form=form)
