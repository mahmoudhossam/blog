from flask import Flask
from config import login 
from mongoengine import connect

app = Flask(__name__)
connect(login['db'], host=login['host'], port=login['port'], \
        username=login['user'], password=login['password'])

import webapp.views, webapp.models
