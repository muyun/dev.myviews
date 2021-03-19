from flask import Blueprint, render_template

#from flask_flatpages import FlatPages

bp = Blueprint('info', __name__)

from . import pages

@bp.route('/link')
def link():
    return render_template('info/link.html', pages=pages)

@bp.route('/proj')
def proj():
    #return 'research'
    return render_template('info/proj.html', pages=pages)

@bp.route('/book')
def book():
    return render_template('info/book.html', pages=pages)

@bp.route('/about')
def about():
    return render_template('info/about.html', pages=pages)

