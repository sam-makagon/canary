from flask import render_template, request
import flask.ext.restless
from pprint import pprint

from conureboard import app, models
from conureboard.database import session, printquery
from conureboard.paginate import get_page_info

manager = flask.ext.restless.APIManager(app, session=session)
service_blueprint = manager.create_api(models.Service)
service_blueprint = manager.create_api(models.Event)
