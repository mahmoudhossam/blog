import bcrypt
from models import Post, User
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

def parse_id(identifier):
    parts = identifier.split('/')
    if len(parts) ==  4:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        slug = parts[3]
        return year, month, day, slug
    return None

def get_post(ID):
    parsed = parse_id(ID)
    if parsed:
        year, month, day, s = parse_id(ID)
        d = date(year, month, day)
        posts = Post.objects(date=d, slug=s)
        return posts.first()
    else:
        return None
