from flask import (
    Flask,
    Blueprint,
    render_template,
    url_for,
    redirect,
    g,
    request,
    session,
    flash
)

from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():

    if g.user:
        return redirect(url_for('posts.posts'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()

        error = None

        if not username:
            error = "Username is required"
        elif not password:
            password = "Password is required"

        if error is None:
            try:
                db.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} already exists"
            else:
                return redirect(url_for('auth.login'))
        
        flash(error)
    
    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():

    if g.user:
        return redirect(url_for('posts.posts'))

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        error = None
        db = get_db()

        user = db.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchone()

        if user is None:
            error = f"Username with {username} not exists"
        elif not check_password_hash(pwhash=user['password'], password=password):
            error = "Incorrect password"
        
        if error is None:
            session.clear()
            session['user_id'] = user['user_id']
            return redirect(url_for('posts.posts'))
    
        flash(error)
    
    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('base'))
