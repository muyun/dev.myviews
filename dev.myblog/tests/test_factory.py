#from context import client, app
import pytest

from context import blog
from blog.app import app, pages

@pytest.fixture # contains setup functions called fixtures that each test will use
def client(app):
    return app.test_client()

"""
@pytest.fixture  # contains setup functions called fixtures that each test will use
def app():
    app = blog.create_app({
        'TESTING': True,
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_config():
    assert not blog.create_app().testing
    assert blog.create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
"""