from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route('/login')
def log_in():
    return '<p>This will be a log in page</p>'

@auth.route('/signup')
def sign_up():
    return '<p>This will be a sign up page</p>'

@auth.route('/logout')
def log_out():
    return '<p>This will be a log out page</p>'