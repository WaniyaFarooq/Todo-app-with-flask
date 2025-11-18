from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("USERNAME",validators=[DataRequired(),Length(min=3,max=25)])
    password = PasswordField("PASSWORD",validators=[DataRequired()])
    submit = SubmitField("Login")
    
    
   


