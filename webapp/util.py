import bcrypt
from models import Post

def validate(user, password):
    hashed = '$2a$12$leF7cVimpflh2P97U4WV8ugjE9HE5fwyeb5shGXjVvFuJoxSj08cC'
    return bcrypt.hashpw(password, hashed) == hashed and user == 'mhh91'

def create_post(title, content):
    Post(title=title, content=content, ID=Post.objects.count() + 1).save()

def all_posts():
    return Post.objects

