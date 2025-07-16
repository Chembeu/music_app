# auth/routes.py
from flask import render_template, redirect, url_for, flash
from . import auth_bp
from ..forms import RegistrationForm

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Add user registration logic here
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)
