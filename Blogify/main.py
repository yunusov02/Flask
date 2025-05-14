import os
from dotenv import load_dotenv


from flask import (
    render_template,
    Flask,
    Blueprint,
    session,
    g,
    get_flashed_messages,
)


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
 

from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


# Registering Blueprints
from apps import user_blueprint
app.register_blueprint(user_blueprint)



# The database Teardown
from database.basemodel import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def base():
    return render_template('home.html')



