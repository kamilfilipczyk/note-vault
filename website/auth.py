from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET','POST'])
def log_in():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password_hash, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again.', category='error')
        else:
            flash('Incorrect email, please try again.', category='error')
    return render_template('login.html', user=current_user)

@auth.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        user_name = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('This email is already in use.', category='error')
        elif len(email) < 5:
            flash('Your email is too short.', category='error')
        elif len(user_name) < 2:
            flash('Your username is too short.', category='error')
        elif len(password) < 8:
            flash('Password must be at least 8 character length', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match.', category='error')
        else:
            new_user = User(email=email, username=user_name, password_hash=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created succesfully!', category='success')
            return redirect(url_for('views.home'))

    return render_template('signup.html', user=current_user)

@auth.route('/logout')
@login_required
def log_out():
    logout_user()
    return render_template('logout.html')