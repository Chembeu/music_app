from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from . import auth_bp
from .forms import LoginForm, RegistrationForm
from app.models import User
from app import db
# from app.email import send_confirmation_email

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.home'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered', 'error')
            return redirect(url_for('auth.register'))
        
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data),
            confirmed=False  # Email confirmation required
        )
        
        db.session.add(user)
        db.session.commit()
        
        # Send confirmation email
        # token = user.generate_confirmation_token()
        # send_confirmation_email(user.email, token)
        
        flash('A confirmation email has been sent to your email address.', 'info')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/signup.html', form=form)

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.home'))
    
    if current_user.confirm(token):
        db.session.commit()
        flash('Account confirmed!', 'success')
    else:
        flash('The confirmation link is invalid or has expired.', 'error')
    
    return redirect(url_for('main.home'))

@auth_bp.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')