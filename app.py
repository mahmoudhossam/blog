from flask import Flask
from flask import render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config.from_pyfile('flask-config.cfg')
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html', posts=all_posts()) 

@app.route('/post/<int:id>')
def get_post(id):
    return render_template('post.html')

def all_posts():
    return mongo.db.posts.find()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
