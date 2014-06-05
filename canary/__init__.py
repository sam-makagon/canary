from __future__ import print_function
import sys
from flask import Flask

app = Flask(__name__)

EVENT_START = 0
EVENT_STOP  = 1
EVENT_INFO  = 2

def logmsg(msg):
  print (msg, file=sys.stderr)

from canary import database, models, views, api, config
