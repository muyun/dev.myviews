#from context import client, app
import pytest

from .context import blog
from blog import create_app

@pytest.fixture  # contains setup functions called fixtures that each test will use
def app():
    app = create_app({
        'TESTING': True,
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()


def test_config():
    assert not create_app().testing

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'