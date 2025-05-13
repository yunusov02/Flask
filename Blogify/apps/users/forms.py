from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(FlaskForm):

    username = StringField(
        "Enter a Username", 
        validators=[
            DataRequired(), 
            Length(5, 30)
        ]
    )

    email = EmailField(
        "Enter your email", 
        validators=[
            DataRequired(), 
            Email()
        ]
    )
    
    password = PasswordField(
        "Enter your password", 
        validators=[
            DataRequired(), 
            Length(min=6, message="Password must be at least 6 character long")
        ]
    )

    confirm = PasswordField(
        "Confirm your password", 
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match")
        ]
    )



class LoginForm(FlaskForm):

    username = StringField(
        "Enter a Username", 
        validators=[
            DataRequired(), 
            Length(5, 30)
        ]
    )
    
    password = PasswordField(
        "Enter your password", 
        validators=[
            DataRequired(), 
            Length(min=6, message="Password must be at least 6 character long")
        ]
    )

