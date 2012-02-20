from mongoengine import *

class Post(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    published_at = DateTimeField(required=True)
    slug = StringField(required=True) 

class User(Document):
    username = StringField(required=True, min_length=4)
    hashed_pw = StringField(required=True)
