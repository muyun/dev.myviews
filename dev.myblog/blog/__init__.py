import os

from flask import Flask
from flask_flatpages import FlatPages
from flaskext.markdown import Markdown
pages = FlatPages()

def create_app(test_config=None):
    app = Flask(__name__)

    #if test_config is None:
    app.config.from_pyfile('config.py')
    #else:
    #    app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    Markdown(app, extensions=['fenced_code'])
    pages.init_app(app)

    from . import blog
    app.register_blueprint(blog.bp)
    #app.add_url_rule('/', endpoint='index')

    from . import info
    app.register_blueprint(info.bp)

    return app

