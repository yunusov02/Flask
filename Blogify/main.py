from flask import (
    render_template,
    Flask,
    Blueprint,
    session,
    g,
    get_flashed_messages,
)

app = Flask(__name__)


# Automatically remove database sessions at the end of the request or when the application is shut down
from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def base():
    return render_template('home.html')



