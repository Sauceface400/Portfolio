from flask_wtf import FlaskForm
from wtforms import StringField ,IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo

#this to create the form so that we can enter the marks for the subjects
class RegistrationForm(FlaskForm):
    username = StringField('Username' ,validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm_password' ,validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

#this is to continue to the home page and delete the data in the database table
class redo(FlaskForm):
    btn = SubmitField("Continue")