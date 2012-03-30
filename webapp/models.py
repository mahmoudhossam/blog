from mongoengine import *

class Post(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    date = DateTimeField(required=True)
    #time = StringField(required=True)
    slug = StringField(required=True) 

class User(Document):
    username = StringField(required=True, min_length=4)
    hashed_pw = StringField(required=True)
    email = StringField(required=True)
