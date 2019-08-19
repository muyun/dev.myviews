import os

from flask import Flask

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'insightmark.sqlite'),
)


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

#from . import database
import database
database.init_app(app)

#from .app import auth
import auth
app.register_blueprint(auth.bp)

#from .app import insightmark
import post
app.register_blueprint(post.bp)
app.add_url_rule('/', endpoint='index')

if __name__ == '__main__':
    app.run()