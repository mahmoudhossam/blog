import bcrypt
from models import *
from slugify import slugify
from datetime import datetime, date

def validate(user, password):
    hashed = '$2a$12$leF7cVimpflh2P97U4WV8ugjE9HE5fwyeb5shGXjVvFuJoxSj08cC'
    return bcrypt.hashpw(password, hashed) == hashed and user == 'mhh91'

def login(user, password):
    results = Post.objects(username=user)
    if len(results) != 0:
        user = results.first()
        return bcrypt.hashpw(password, user.hashed_pw) == user.hashed_pw

def create_post(title, content, date=date.today()):
    slug = slugify(title)
    post = Post(title=title, content=content, date=date, slug=slug)
    post.save()

def all_posts():
    return Post.objects

def get_post(year, month, day, slug):
    date = date(year, month, day)
    posts = Post.objects(date=date)
    for i in posts:
        if i.slug == slug:
            return i

