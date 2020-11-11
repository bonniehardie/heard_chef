from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SubmitField, PasswordField
)
from wtforms.validators import DataRequired, ValidationError

v = [DataRequired()]

class LoginForm(FlaskForm):
    employee_number = StringField('Employee number', v)
    password = PasswordField('Password', v)
    submit = SubmitField('Login')
