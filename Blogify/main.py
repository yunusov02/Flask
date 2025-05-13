from flask import (
    render_template,
    Flask,
    Blueprint,
    session,
    g,
    get_flashed_messages,
)

from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

app = Flask(__name__)

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


# Registering Blueprints
from apps import user_blueprint
app.register_blueprint(user_blueprint)



# The database Threadown
from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def base():
    return render_template('home.html')



