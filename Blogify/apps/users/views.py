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
    form = RegistrationForm()

    if request.method == 'POST':
        pass

    context = {"form": form}

    return render_template("users/registration.html", context=context)








