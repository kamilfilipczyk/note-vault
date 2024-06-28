from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET','POST'])
def log_in():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    return render_template('login.html')

@auth.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        user_name = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        """
        if len(email) < 5:
            flash('Your email is too short.', category='error')
        elif len(user_name) < 2:
            flash('Your username is too short.', category='error')
        elif len(password) < 8:
            flash('Password must be at least 8 character length', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match.', category='error')
        else:
            flash('Account created succesfully!', category='success')
            
        """
    return render_template('signup.html')

@auth.route('/logout')
def log_out():
    return render_template('logout.html')