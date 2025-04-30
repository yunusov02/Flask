from flask import (
    Flask,
    Blueprint,
    g,
    redirect,
    url_for,
    flash,
    session,
)


bp = Blueprint('likes', __name__, url_prefix='/likes')


@bp.route('/create', methods=['GET', 'POST'])
def create_likes():
    pass




