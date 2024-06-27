from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route('/login')
def log_in():
    return render_template('login.html')

@auth.route('/signup')
def sign_up():
    return render_template('signup.html')

@auth.route('/logout')
def log_out():
    return render_template('logout.html')