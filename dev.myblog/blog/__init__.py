import os

from flask import Flask,render_template_string
from flask_flatpages import FlatPages, pygments_style_defs
from flask_flatpages.utils import pygmented_markdown
from flaskext.markdown import Markdown
pages = FlatPages()

def my_renderer(text):
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/pygments.css')
    def pygments_css():
        return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

    app.config['FLATPAGES_HTML_RENDERER'] = my_renderer
    Markdown(app, extensions=['fenced_code'])
    pages.init_app(app)

    from . import blog
    app.register_blueprint(blog.bp)
    #app.add_url_rule('/', endpoint='index')

    from . import info
    app.register_blueprint(info.bp)

    return app

