from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import User

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