# auth/routes.py
from flask import render_template, redirect, url_for, flash
from . import auth
from ..forms import DJForm


@auth.route('/add_dj', methods=['GET', 'POST'])
def add_dj():
    form = DJForm()
    if form.validate_on_submit():
        # Add DJ creation logic here
        flash('DJ added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_dj.html', form=form)
