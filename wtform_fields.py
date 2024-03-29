from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    """ Registration form"""
    username =  StringField('username_label', validators=[InputRequired(message='Username required'), Length(min=4, max=25, message='Username must be between 4 and 25 characters')])
    password = PasswordField('password_label',  validators=[InputRequired(message='Password required'), Length(min=4, max=25, message='Password must be between 4 and 25 characters')])
    confirm_pswd = PasswordField('confirm_pswd_label',  validators=[InputRequired(message='Password required'), EqualTo('password', message='Passwords must match')])
    submit_button  = SubmitField('Register')


    def validate_username(self, username):
        """ Validate username"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')