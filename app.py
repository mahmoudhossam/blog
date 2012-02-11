from flask import Flask, request, redirect, url_for
from flask import render_template
from mongoengine import *
from datetime import datetime
import os, bcrypt, config

# Initialization:
###################################################################
app = Flask(__name__)
connect(config.DBNAME, host=config.HOST, port=config.PORT, \
        username=config.USERNAME, password=config.PASSWORD)

# Models:
###################################################################
class Post(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    published_at = datetime.utcnow()
    ID = IntField(min_value=1)

def create_post(title, content):
    Post(title=title, content=content, ID=Post.objects.count() + 1).save()

def all_posts():
    return Post.objects

# VIEWS:
####################################################################
@app.route('/')
def index():
    return render_template('index.html', posts=all_posts()) 

@app.route('/post/<int:id>')
def get_post(id):
    return render_template('post.html')

@app.route('/new', methods=['POST', 'GET'])
def post_new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['body']
        create_post(title, content)
        return "Post created."
    else:
        return render_template('new.html')

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

################################################################################

def validate(user, password):
    hashed = '$2a$12$leF7cVimpflh2P97U4WV8ugjE9HE5fwyeb5shGXjVvFuJoxSj08cC'
    return bcrypt.hashpw(password, hashed) == hashed and user == 'mhh91'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Disable this when deploying
    app.debug = True
    app.run(host='0.0.0.0', port=port)
