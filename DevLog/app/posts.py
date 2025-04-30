import functools

from flask import (
    Flask,
    url_for,
    redirect,
    render_template,
    Blueprint,
    request,
    session,
    flash
)

from app.db import get_db


bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.context_processor
def inject_categories():
    db = get_db()
    categories = db.execute('SELECT * FROM category').fetchall()
    return {'categories': categories}


@bp.route('/', methods=['GET'])
def posts():
    db = get_db()
    error = None

    if request.method == "GET":
        category_id = request.args.get('category', '0')

        if category_id == '0':
           posts = db.execute('select * from posts').fetchall()
        else:
            posts = db.execute('SELECT * FROM posts WHERE category_id = ?', (category_id, )).fetchall()

    return render_template('posts/posts.html', posts=posts)


@bp.route('/create', methods=['GET', 'POST'])
def create_post():
    db = get_db()
    error = None

    if request.method == "POST":

        print(request.form)

        title = request.form['title']
        body = request.form['body']
        category = request.form['category']
        published = 1 if request.form.get('publish') == 'on' else 0
        user_id = session.get('user_id')

        if category == "0":
            error = "Please select one category."
        elif not title or not body:
            error = "Please fill the post title and body."
        else:
            db.execute(
                "INSERT INTO posts (user_id, category_id, title, body, published) VALUES (?, ?, ?, ?, ?)",
                (user_id, category, title, body, published)
            )
            db.commit()

            return redirect(url_for('posts.posts'))

    if error:
        flash(error)

    return render_template('posts/post_create.html')


@bp.route("/detail/<int:id>", methods=['GET', 'POST'])
def detail_post(id):
    db = get_db()
    error = None
    
    post = db.execute("SELECT * FROM posts WHERE post_id = ?", (id,)).fetchone()

    if post is None:
        error = "There is no post like this"
        return redirect(url_for("posts.posts"))

    if error:
        flash(error)

    context = {
        "post": post,
        "user": db.execute("SELECT * FROM users WHERE user_id = ?", (post['user_id'], )).fetchone()['username']
    }

    return render_template("posts/post_detail.html", context=context)


@bp.route("/update/<int:id>", methods=['GET', 'POST'])
def update_post(id):
    db = get_db()
    error = None
    
    post = db.execute("SELECT * FROM posts WHERE post_id = ?", (id,)).fetchone()

    if post is None:
        error = "There is no post like this"
        return redirect(url_for("posts.posts"))


    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        published = 1 if request.form.get('publish') == 'on' else 0

        if post['user_id'] != session.get('user_id'):
            flash(error)
            return redirect(url_for('posts.update_post', id=id))

        db.execute(
            'UPDATE posts '
            'SET title = ?, body = ?, published = ?'
            'WHERE post_id = ?',
            (title, body, published, id)
        )
        db.commit()
        
        return redirect(url_for('posts.detail_post', id=id))

    if error:
        flash(error)

    return render_template("posts/post_update.html", post=post)


@bp.route('/delete_post/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    db = get_db()
    error = None
    
    db.execute("DELETE FROM  posts WHERE post_id = ? ", (id,))
    db.commit()

    flash("The post deleted Successfully")

    return redirect(url_for("posts.posts"))
