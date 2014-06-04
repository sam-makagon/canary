from flask import Flask

app = Flask(__name__)

from canary import database, models, views, api, config
