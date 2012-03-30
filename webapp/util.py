import bcrypt
from models import Post, User
from slugify import slugify
from datetime import datetime, date

def validate(password, user):
    hashed = user.hashed_pw
    return bcrypt.hashpw(password, hashed) == hashed

def login(user, password):
    result = User.objects(username=user)
    if result:
        usr = result.first()
        return validate(password, usr.username)

def create_post(title, content, date=date.today()):
    slug = slugify(title)
    post = Post(title=title, content=content, date=date, slug=slug)
    post.save()

def create_user(user, password, email):
    usr = User(username=user, password=password, email=email)
    User.save()

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
