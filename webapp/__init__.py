from flask import Flask
import config
from mongoengine import connect

app = Flask(__name__)
connect(config.DBNAME, host=config.HOST, port=config.PORT, \
        username=config.USERNAME, password=config.PASSWORD)

import webapp.views, webapp.models
