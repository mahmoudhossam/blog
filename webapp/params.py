import os, re

_url = os.getenv('MONGOLAB_URI')
_tokens = re.split('[:/@]', _url)

#eliminate empty and unused tokens
del _tokens[:4]

login = {
    'user' : _tokens[3],
    'password' : _tokens[0],
    'host' : _tokens[1],
    'port' : int(_tokens[2]),
    'db' : _tokens[3]
    }
