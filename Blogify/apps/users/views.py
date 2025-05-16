import functools

from flask import (
    Blueprint,
    flash,
    get_flashed_messages,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash,   check_password_hash

from .models import User
from .forms import LoginForm, RegistrationForm
from database.basemodel import db_session
from ..decorator import login_required

user_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():

    if 'user_id' in session:
        flash("You are already logged in.", "info")
        return redirect(url_for('base'))

    form = RegistrationForm()

    if request.method == "POST" and form.validate():
        try:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data)
            )

            db_session.add(user)
            db_session.commit()
            
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('auth.login'))

        except IntegrityError:
            
            db_session.rollback()
            flash("This username or email already exists.", "danger")
            return redirect(url_for('auth.register'))

    if form.errors:
        flash(form.errors, "danger")

    return render_template("users/registration.html", form=form)



@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    if 'user_id' in session:
        flash("You are already logged in.", "info")
        return redirect(url_for('base'))

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        user = db_session.query(User).filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session.clear()
            session['user_id'] = user.id
            flash("Login successful!", "success")
            return redirect(url_for('base'))
        else:
            flash("Invalid username or password.", "danger")    
            return redirect(url_for('base')) 

    return render_template("users/login.html", form=form)


@login_required
@user_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('base'))


@login_required
@user_blueprint.route('/profile')
def profile():
    if 'user_id' not in session:
        flash("You need to log in to access your profile.", "info")
        return redirect(url_for('auth.login'))

    user = db_session.query(User).filter_by(id=session['user_id']).first()

    return render_template("users/profile.html", user=user)



