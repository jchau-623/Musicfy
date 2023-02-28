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


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')

def repeat_email(form, field):
    repeat_email = field.data
    email = form.data['email']

    if not repeat_email == email:
        raise ValidationError("Your emails must match.")

def password_length(form, field):
    password = field.data
    if len(password) < 5 or len(password) > 20:
        raise ValidationError('Password must be between 5 and 20 characters.')



class SignUpForm(FlaskForm):
    email = StringField('email', validators=[DataRequired('You need to enter your email.'), user_exists, Length(min=3, max=255, message='Email must be between 3 and 255 characters.')])
    repeat_email = StringField('email', validators=[DataRequired('You need to confirm your email.')])
    password = StringField('password', validators=[DataRequired('You need to enter a password.')])
    username = StringField(
        'username', validators=[DataRequired('Enter a name for your profile.'), username_exists,Length(min=3, max=40, message='Username must be between 3 and 30 characters.')])
