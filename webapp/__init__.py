from flask import Flask
from params import login 
from mongoengine import connect

app = Flask(__name__)
connect(login['db'], host=login['host'], port=login['port'], \
        username=login['user'], password=login['password'])

# Disable this when deploying
app.debug = True

import webapp.views, webapp.models
