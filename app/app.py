from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('../config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}@{app.config['DB_HOST']}/{app.config['DB_NAME']}"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_uid):
        return User.query.get(int(user_uid))

    # blueprint for routes in our app
    from app.views.index import bp as bp_index
    app.register_blueprint(bp_index)

    from app.views.login import bp as bp_login
    app.register_blueprint(bp_login)

    from app.views.logout import bp as bp_logout
    app.register_blueprint(bp_logout)

    from app.views.register import bp as bp_register
    app.register_blueprint(bp_register)

    from app.views.add_offer import bp as bp_add_offer
    app.register_blueprint(bp_add_offer)

    from app.views.about import bp as bp_about
    app.register_blueprint(bp_about)

    from app.views.profile import bp as bp_profile
    app.register_blueprint(bp_profile)

    from app.views.offer import bp as bp_offer
    app.register_blueprint(bp_offer)

    with app.app_context():
        db.create_all()

    return app
