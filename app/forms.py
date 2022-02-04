from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
# from .models import User

class PokemonForm(FlaskForm):
    name = StringField('Pokemon Name', validators=[DataRequired()])
    submit = SubmitField('PokeGoGo!!')
    
class LoginForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class RegistrationForm(FlaskForm):
    name_first = StringField('Name First', validators=[DataRequired()])
    name_last = StringField('Name Last', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Re-enter Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')
    
# add email validation function