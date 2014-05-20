import flask.ext.restless

from conureboard import app, models
from conureboard.database import session

manager = flask.ext.restless.APIManager(app, session=session)
service_blueprint = manager.create_api(models.Service, methods=['GET', 'PUT', 'POST'])
service_blueprint = manager.create_api(models.Event, methods=['GET', 'PUT', 'POST'])
