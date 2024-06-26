# import Flask class from flask package
from flask import Flask

def create_app():
    # create new instance of the Flask class and assign it to "app" variable
    app = Flask(__name__)
    # set the secret key which will be used for securing data
    app.config['SECRET_KEY'] = "nyarlathotep"
    # in order to register our blueprints its necessary to import them first
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')

    # return the configured instance of the Flask class
    return app

