import os
import pytest

from context import blog
from blog.app import app, pages

def test_flatpages():
    source = os.path.join(os.path.dirname(__file__), 'pages')
    app.config['FLATPAGES_EXTENSION'] = '.md'
    app.config['FLATPAGES_ROOT'] = source

    hello = pages.get('hello')
    assert hello.meta['title'] == b'Hello'

if __name__ == "__main__":
    test_flatpages()