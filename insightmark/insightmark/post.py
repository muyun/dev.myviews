from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from sqlalchemy import desc


#from app.auth import login_required
#from app.database import get_db
from auth import login_required
#from database import get_db
from models import db, User, Post


bp = Blueprint('post', __name__)

@bp.route('/')
def index():
    """
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    """
    #print("check_author-: ", check_author)
    posts = Post.query.filter(Post.author_id == User.id).order_by(desc(Post.created))
    #print("posts-: ", posts)

    return render_template('post/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            """
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            """
            #print("g.user.id: ",g.user.id)
            #print("title: ", title)
            #print("body: ", body)
            _post = Post( g.user.id, title, body)
            db.session.add(_post)
            db.session.commit()

            return redirect(url_for('post.index'))

    return render_template('post/create.html')

def get_post(id, check_author=True):
    """
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()
    """
    #print("id: ", id)
    post = Post.query.filter(Post.id == id).first()
    #print("post: ", post)
    #print("post.id: ", post.id)

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    print("check_author: ", check_author)
    print("post.id: ", post.id)
    print("g.user.id: ", g.user.id)

    """
    if check_author and post.id != g.user.id:
        abort(403)
    """
    
    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            """
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            """
            _post = Post.query.filter(Post.id == id).first()
            db.session.delete(_post)

            post = Post(g.user.id, title, body)
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('post.index'))

    return render_template('post/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)

    """
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    """
    post = Post.query.filter(Post.id == id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('post.index'))