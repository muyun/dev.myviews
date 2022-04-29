import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.SQLAlchemy import SQLAlchemy

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY='dev',
    #DATABASE=os.path.join(app.instance_path, 'insightmark.sqlite'),   
)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://uligqnruzxurss:b427d869c5bced80eb8b413707d25c0e15ad81dbad80fd809ec76de0a9dd39dc@ec2-174-129-252-252.compute-1.amazonaws.com:5432/d6op0ied1i4pua'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/zhaowenlong'

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

#from . import database
"""
import database
database.init_app(app)
"""
from models import db
db.init_app(app)

#from .app import auth
import auth
app.register_blueprint(auth.bp)

#from .app import insightmark
import post
app.register_blueprint(post.bp)
app.add_url_rule('/', endpoint='index')

if __name__ == '__main__':
    app.debug = True
    app.run()