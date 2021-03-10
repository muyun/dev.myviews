import os
import logging
import pytest

from flask import request, url_for

from context import blog
from blog.app import app, pages

def test_app_hello():
    with app.test_request_context('/hello', method='POST'):
        #print(url_for('hello'))
        assert request.path == '/hello'
        
        hello = pages.get('hello')
        assert hello.meta['title'] == b'Hello'