from flask import Blueprint, render_template,redirect, flash, url_for, request
from flask_login import login_required, current_user
from app.models import User
from app.forms import MixForm
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from app.models import Mix
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def home():
     if hasattr(current_user, 'first_name') and hasattr(current_user, 'last_name'):
        initials = f"{current_user.first_name[0]}{current_user.last_name[0]}".upper()
     else:
        initials = "?" 
     return render_template('index.html', user=current_user, initials=initials)

@main_bp.route('/profile')
@login_required
def my_profile():
    return render_template('profile.html', user=current_user)

@main_bp.route('/profile/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', user=user)
@main_bp.route('/add_mix', methods=['GET', 'POST'])
def add_mix():
    form = MixForm()
    if form.validate_on_submit():
        # Handle file upload
        file = form.file.data
        filename = secure_filename(file.filename)
        upload_folder = os.path.join('app', 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        # Create Mix instance
        mix = Mix(
            name=form.name.data,
            date_uploaded=datetime.strptime(form.date_uploaded.data, "%Y-%m-%d"),
            stream=int(form.stream.data) if form.stream.data else 0,
            downloads=int(form.downloads.data) if form.downloads.data else 0,
            file_path=file_path,
            file_size=os.path.getsize(file_path),
            # duration can be set if you process the audio file
        )
        db.session.add(mix)
        db.session.commit()
        flash('Mix added successfully!', 'success')
        return redirect(url_for('main.add_mix'))
    return render_template('upload.html', form=form)