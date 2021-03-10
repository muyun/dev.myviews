# contains setup functions called fextures that each test will use 

import os
import tempfile

import pytest

from context import blog
from blog.app import app, pages

@pytest.fixture
def pages():
    source = os.path.join(os.path.dirname(__file__), 'pages')
    app.config['FLATPAGES_ROOT'] = source

    #yield app

"""
from blog import create_app
from blog.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    #print("db_fd:", db_fd)
    #print("db_path:", db_path)

    app = create_app({
        'TESTING': True,  # testing flag
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        db = get_db()

        #print("DATA_SQL:", _data_sql)
        db.executescript(_data_sql)
        #db.commit()
    
    yield app
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()
"""