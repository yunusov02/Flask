import functools

from flask import (
    Blueprint,
    get_flashed_messages,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)


from werkzeug.security import generate_password_hash,   check_password_hash

from .models import User
from .forms import LoginForm, RegistrationForm


user_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            user = User(
                username=form.data['username'],
                email=form.data['email'],
                password=generate_password_hash(form.data['password'])
            )
        
        except:
            pass

    context = {"form": form}

    return render_template("users/registration.html", context=context)



@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST':
        pass

    context = {"form": form}

    return render_template("users/login.html", context=context)







