from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from flask_ckeditor import CKEditorField


from .models import Category
from database.basemodel import db_session


class CreatePost(FlaskForm):

    category = SelectField(
        "Select Category", 
        choices=[(category.id, category.name) for category in db_session.query(Category).all()], 
        validators=[DataRequired()]
    )

    title = StringField(
        "Enter your title", 
        validators=[
            DataRequired(), 
            Length(5, 30, message="Your title must be at least 5 character")
        ]
    )

    body = CKEditorField(
        "Enter your content", 
        validators=[
            DataRequired(), 
            Length(5, 1000, message="Your content must be at least 5 character")
        ]
    )

    is_published = BooleanField(
        "Publish Post",
        default=True, 
        render_kw={
            "class": "form-check-input"
        }
    )

    submit = SubmitField("Create Post", 
        render_kw={
            "class": "btn btn-primary btn-block"
        }
    )
