from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    """docstring for SignupForm"""
    name = StringField('Name', validators = [DataRequired("Please enter your name")])
    email = StringField('Email', validators = [DataRequired("Please enter your email"), Email('gültige email')])
    password = PasswordField('Password', validators = [Length(min=6, message = 'Mindestens 6 Zeichen')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    """docstring for Login"""
    email = StringField('Email', validators = [DataRequired("Please enter your email"), Email('gültige email')])
    password = PasswordField('Password', validators = [DataRequired("Please enter your name")])
    submit = SubmitField('Log in')
