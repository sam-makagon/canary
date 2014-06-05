from __future__ import print_function
import sys
from flask import Flask

app = Flask(__name__)

def logmsg(msg):
  print (msg, file=sys.stderr)

from canary import database, models, views, api, config
