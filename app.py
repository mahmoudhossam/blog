from flask import Flask, request, redirect, url_for
from flask import render_template
from flask.ext.pymongo import PyMongo
import os, bcrypt

app = Flask(__name__)
app.config.from_pyfile('flask-config.cfg')
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html', posts=all_posts(), header="Programming Beans") 

@app.route('/post/<int:id>')
def get_post(id):
    return render_template('post.html')

@app.route('/new', methods=['POST', 'GET'])
def post_new():
    if request.method == 'POST':
        return 'Title: %s' % request.form['title'] + '\n' + \
        'Body: %s' % request.form['body']
    else:
        return render_template('new.html')

def all_posts():
    return mongo.db.posts.find()

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        user = request.form['user']
        if validate(user, password):
            return "Authenticated"
        else:
            return "Invalid user/password."
    else:
        return render_template('login.html')

def validate(user, password):
    hashed = '$2a$12$leF7cVimpflh2P97U4WV8ugjE9HE5fwyeb5shGXjVvFuJoxSj08cC'
    return bcrypt.hashpw(password, hashed) == hashed and user == 'mhh91'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Disable this when deploying
    #app.debug = True
    app.run(host='0.0.0.0', port=port)
