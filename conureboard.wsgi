from conureboard import app as application

import logging
import pprint

class LoggingMiddleware:

  def __init__(self, application):
    self.__application = application

  def __call__(self, environ, start_response):
    errors = environ['wsgi.errors']
    pprint.pprint(('REQUEST', environ), stream=errors)

    def _start_response(status, headers, *args):
      pprint.pprint(('RESPONSE', status, headers), stream=errors)
      return start_response(status, headers, *args)

    return self.__application(environ, _start_response)


#application = LoggingMiddleware(application)

if not application.debug:
  import logging
  from logging.handlers import RotatingFileHandler
  file_handler = RotatingFileHandler('flask.log', maxBytes=1024 * 1024 * 100, backupCount=3)
  file_handler.setLevel(logging.WARNING)
  application.logger.setLevel(logging.WARNING)
  application.logger.addHandler(file_handler)
