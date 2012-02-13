from mongoengine import *
from datetime import datetime

class Post(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    published_at = datetime.utcnow()
    ID = IntField(min_value=1)

