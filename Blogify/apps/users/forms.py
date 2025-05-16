from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(FlaskForm):

    username = StringField(
        "Enter your username", 
        validators=[
            DataRequired(), 
            Length(5, 30, message="Your username must be at least 5 character")
        ]
    )

    email = EmailField(
        "Enter your email", 
        validators=[
            DataRequired(), 
            Email(message="You must enter a valid email")
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

    submit = SubmitField("Register", 
        render_kw={
            "class": "btn btn-primary btn-block"
        }
    )



class LoginForm(FlaskForm):

    username = StringField(
        "Enter your username", 
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

    submit = SubmitField("Lig in", 
        render_kw={
            "class": "btn btn-primary btn-block"
        }
    )
