from flask import Flask

app = Flask(__name__)

from conureboard import database, models, views, api
