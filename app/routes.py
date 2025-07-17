
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html',user=current_user)

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
