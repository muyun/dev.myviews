import os
import logging 

from flask import Flask, render_template, url_for, request
from flask_flatpages import FlatPages

FLATPAGES_AUTO_RELOAD = 'DEBUG'
#FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_pyfile('config_public.py')
pages = FlatPages(app)


@app.route('/hello')
def hello():
    page = pages.get('hello')
    #logging.debug(f'page.meta:{page.meta}')
#    title = page.meta['title']

#    posts = (p for p in pages if 'date' in p.meta)
#    print(posts)
#    sorted(posts,key=lambda p: p.meta['date'], reverse=True)
#    return render_template('page.html', titles=title)
    return "Hello World"

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html',page=page) 

@app.route('/')
def index():
    return render_template('index.html', pages=pages)
  
@app.route('/about')
def about():
    return "About"

if __name__ == "__main__":
    #hello()
    app.run()
    