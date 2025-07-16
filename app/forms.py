# forms.py
# Define your Flask-WTF forms here

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


# Form for DJ model
class DJForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_no = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Add DJ')

# Form for Mix model
from wtforms import FileField

class MixForm(FlaskForm):
    name = StringField('Mix Name', validators=[DataRequired()])
    date_uploaded = StringField('Date Uploaded', validators=[DataRequired()])  # Use DateField if you want date picker
    stream = StringField('Stream', default='0')
    downloads = StringField('Downloads', default='0')
    file = FileField('Upload Mix', validators=[DataRequired()])
    submit = SubmitField('Add Mix')

# Form for User model
class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


