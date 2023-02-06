from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for routes in our app
    from views.index import bp as bp_index
    app.register_blueprint(bp_index)

    from views.login import bp as bp_login
    app.register_blueprint(bp_login)

    from views.register import bp as bp_register
    app.register_blueprint(bp_register)

    return app
