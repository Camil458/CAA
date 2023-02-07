from flask import Blueprint, render_template, request
from werkzeug.security import generate_password_hash

from app.app import db
from app.models import User
from app.views.forms import RegisterForm

bp = Blueprint('register', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():

        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # if this returns a user, then the email already exists in database
        user = User.query.filter_by(email=email, username=username).first()

        if user:
            error = "Username or email already in use"
            return render_template('register.html', form=form, error=error)
        else:
            # create a new user
            new_user = User(name=name, username=username, email=email, password=generate_password_hash(password, method='sha256'))
            
            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            message = "You have been successfully registered. now you can login"
            return render_template('register.html', form=form, message=message)

    return render_template('register.html', form=form)
