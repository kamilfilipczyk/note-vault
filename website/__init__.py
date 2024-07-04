# import Flask class from flask package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "note_vault.db"

def create_app():
    # create new instance of the Flask class and assign it to "app" variable
    app = Flask(__name__)
    # set the secret key which will be used for securing data
    app.config['SECRET_KEY'] = "nyarlathotep"
    # set database location
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # in order to register our blueprints its necessary to import them first

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.log_in'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    # return the configured instance of the Flask class
    return app

def create_db(app):
    with app.app_context():
        db.create_all()