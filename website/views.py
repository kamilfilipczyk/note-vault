from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note_content = request.form.get('noteContent')
        note_title = request.form.get('noteTitle')
        new_note = Note(title=note_title,data=note_content, user_id = current_user.id)
        db.session.add(new_note)
        db.session.commit()

    return render_template("home.html", user=current_user)