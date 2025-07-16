# auth/routes.py
from flask import render_template, redirect, url_for, flash
from . import auth
from ..forms import DJForm, LoginForm


@auth.route('/add_dj', methods=['GET', 'POST'])
def add_dj():
    form = DJForm()
    if form.validate_on_submit():
        # Add DJ creation logic here
        flash('DJ added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_dj.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Add login logic here
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    return render_template('auth/login.html', form=form)
