from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')

def password_check(form, field):
    password = field.data
    special = ['!', '@', '#', '$', '%', '^', '&', '*']
    if len(password) < 6 or len(password) > 20:  # Corrected the maximum length
        raise ValidationError('Password must be between 6 and 20 characters')

    elif not any(x in password for x in special):
        raise ValidationError("Please include at least one of: ! @ # $ % ^ & * ")


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')

def repeat_email(form, field):
    repeat_email = field.data
    email = form.data['email']
    if repeat_email != email:
        raise ValidationError("Emails must match")


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired('Username is required'), username_exists, Length(min=3, max=30, message='Username must be between 3 and 30 characters.')])
    email = StringField('email', validators=[DataRequired('Email address is required'), Email('Email address is invalid'), user_exists, Length(min=3, max=255, message='Email must be between 3 and 255 characters.')])
    password = StringField('password', validators=[DataRequired('Password is required'), password_check])
    repeat_email = StringField('repeat_email', validators=[DataRequired('Please confirm your email'), repeat_email])
