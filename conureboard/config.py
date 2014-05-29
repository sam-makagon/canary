import os
from ConfigParser import SafeConfigParser,NoOptionError
basedir = os.path.abspath(os.path.dirname(__file__))
parser = SafeConfigParser()
parser.read('conureboard/conureboard.cfg')

#SQLAlchemy database connection string
try:
  DB_ENGINE = parser.get('DEFAULT','DB_ENGINE')
except NoOptionError:
  DB_ENGINE = 'sqlite:///' + os.path.join(basedir, 'app.db')

#how many items per page to display on service and events pages
try:
  ITEMS_PER_PAGE = parser.get('DEFAULT','ITEMS_PER_PAGE')
except NoOptionError:
  ITEMS_PER_PAGE = 50

#log sql statements and arguments to STDERR; flask.log when running under WSGI
try:
  DEBUG = parser.get('DEFAULT','DEBUG')
except NoOptionError:
  DEBUG = 0