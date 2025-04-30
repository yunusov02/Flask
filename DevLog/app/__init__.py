import os

from flask import Flask, render_template, g, session

from . import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #   instance_relative_config=True 
    #   Tells Flask that configuration files are relative to
    #   to the instance folder which is located outside of the main sources

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def base():
        return render_template('home.html')
    
    @app.before_request
    def load_logged_in_user():
        user_id = session.get('user_id')

        if user_id is None:
            g.user = None
        else:
            g.user = db.get_db().execute(
                'SELECT * FROM users WHERE user_id = ?',
                (user_id,)
            ).fetchone()

    db.init_app(app)

    from . import posts
    app.register_blueprint(posts.bp)

    from . import auth
    app.register_blueprint(auth.bp)


    return app


