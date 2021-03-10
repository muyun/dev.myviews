from flask import Blueprint, render_template

from flask_flatpages import FlatPages
bp = Blueprint('blog', __name__)

from . import create_app

app = create_app({
        'TESTING': True,  # testing flag
        #'DATABASE': db_path,
    })

pages=FlatPages(app)

POST_DIR = 'posts'
#FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

@bp.route("/")
def posts():
    posts = [p for p in pages if 'title' in p.meta]
    print(posts)
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('posts.html', posts=posts)

@bp.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = pages.get_or_404(path)
    return render_template('post.html', post=post)

