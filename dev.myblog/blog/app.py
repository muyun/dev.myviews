import os
from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_mapping(
        TESTING=True,
        SECRET_KEY='dev',
        #DATABASE = os.path.join(app.instance_path, 'blog.sqlite'),
    )

pages = FlatPages(app)
FLATPAGES_INSTANCE_RELATIVE=True
#FLATPAGES_ROOT = 'posts'
FLATPAGES_EXTENSION = ['.md', '.markdown']
#FLATPAGES_AUTO_RELOAD = DEBUG

@app.route("/")
def index():
    print(pages)
    posts = [p for p in pages if 'date' in p.meta]
    print(posts)
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('posts.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
