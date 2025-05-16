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
from database.basemodel import db_session
from ..users.models import User

from .models import Post
from .forms import CreatePost

from ..decorator import login_required


post_bluprint = Blueprint('posts', __name__, url_prefix='/posts')




@login_required
@post_bluprint.route('/user_posts:<int:id>', methods=['GET', 'POST'])
def user_posts(id):

    user = db_session.query(User).filter_by(id=id).first()

    posts = db_session.query(Post).filter_by(user_id=user.id, is_published=True).all()

    return render_template("posts/user_posts.html", posts=posts, user=user)


@login_required
@post_bluprint.route('/create', methods=['GET', 'POST'])
def create_post():

    form = CreatePost()

    if request.method == 'POST':
        user_id = session['user_id']
        post = Post(
            category_id=request.form.get('category'),
            title=request.form.get('title'), 
            body=request.form.get('content'), 
            is_published=request.form.get('is_published') == 'on', 
            user_id=session['user_id']
        )

        db_session.add(post)
        try:
            db_session.commit()
            flash("Post created successfully!", "success")
            return redirect(url_for('posts.user_posts', id=user_id))
        except IntegrityError:
            db_session.rollback()
            flash("An error occurred while creating the post.", "danger")

    return render_template("posts/create_post.html", form=form)

