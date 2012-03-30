from webapp import app
from flask import Flask, request, redirect, url_for, render_template, abort
from models import Post
from util import *

@app.route('/')
def index():
    return render_template('index.html', posts=all_posts())

@app.route('/post/<path:ID>/')
def render_post(ID):
    post = get_post(ID)
    if post:
        return render_template('post.html', post=post)
    else:
        abort(404)

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

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        password = request.form['password']
        user = request.form['user']
        email = request.form['email']
        if user and password and email:
            create_user(user, password, email)
        else:
            #This is temporary, until I figure something else out.
            abort(404)
