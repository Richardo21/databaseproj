from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField, TextAreaField, StringField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField 
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    uname = StringField('Username', validators=[InputRequired()])
    pword = PasswordField('Password', validators=[InputRequired()])

class RegistrationForm(FlaskForm):
    uname = StringField('Username', validators=[InputRequired()])
    pword = PasswordField('Password', [validators.DataRequired(),
    validators.EqualTo('confirm',message='Passwords must match.')])
    confirm = PasswordField('Confirm Password')
    crdcardno = TextField('Credit Card Number', validators = [InputRequired()])

class Search(FlaskForm):
    searchTerm = StringField('<h5>Search for an item</h5>')

class Report(FlaskForm):
    name = TextField('Branch Name', validators = [InputRequired()])