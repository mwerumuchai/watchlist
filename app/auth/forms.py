from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email=StringField('your email address',validators=[Required(),Email()])
    username=StringField('your username',validators=[Required()])
    password=PasswordField("password",validators=[Required(),
    EqualTo('password',message='passwords must match')])
    password_confirm=PasswordField('confirm password',validators=[Required()])
    submit=SubmitField('sign Up')


    def validator_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('there is an account with that email')

    def validator_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('that user name is taken')

class LoginForm(FlaskForm):
    email=StringField('your email address',validators=[Required(),Email()])
    password=PasswordField('password',validators=[Required()])
    remember = BooleanField('remember me')
    submit=SubmitField('sign in')
