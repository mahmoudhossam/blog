import bcrypt
from models import Post, User
from slugify import slugify
from datetime import datetime

def validate(user, password):
    hashed = '$2a$12$leF7cVimpflh2P97U4WV8ugjE9HE5fwyeb5shGXjVvFuJoxSj08cC'
    return bcrypt.hashpw(password, hashed) == hashed and user == 'mhh91'

def login(user, password):
    results = Post.objects(username=user)
    if len(results) != 0:
        user = results.first()
        return bcrypt.hashpw(password, user.hashed_pw) == user.hashed_pw

def create_post(title, content, published_at=datetime.today()):
    slug = slugify(title)
    post = Post(title=title, content=content, \
            published_at=published_at, slug=slug)
    post.save()

def all_posts():
    return Post.objects

def get_post(year, month, day, slug):
    date = datetime(year, month, day)
    post = Posts.objects(published_at=date, slug=slug)
    return post.first()

