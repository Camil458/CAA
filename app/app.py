from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('../config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}@{app.config['DB_HOST']}/{app.config['DB_NAME']}"

    db.init_app(app)

    # blueprint for routes in our app
    from app.views.index import bp as bp_index
    app.register_blueprint(bp_index)

    from app.views.login import bp as bp_login
    app.register_blueprint(bp_login)

    from app.views.register import bp as bp_register
    app.register_blueprint(bp_register)

    return app
