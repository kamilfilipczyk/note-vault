# import Flask class from flask package
from flask import Flask

def create_app():
    # create new instance of the Flask class and assign it to "app" variable
    app = Flask(__name__)
    # set the secret key which will be used for securing data
    app.config['SECRET_KEY'] = "nyarlathotep"

    # return the configured instance of the Flask class
    return app