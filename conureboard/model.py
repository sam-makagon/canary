from conureboard.database import db, metadata, session
from sqlalchemy import Table
from pprint import pprint


statusTable = Table('statuses', metadata, autoload=True)
serviceTable = Table('services', metadata, autoload=True)
eventTable = Table('events', metadata, autoload=True)

statuses = {}
for (status_id, name) in session.query(statusTable).all():
    statuses[status_id] = name

#pprint(vars(statusTable))

#class Status

#for key in statuses.all():
#    print "%s=%s" % (key, statuses[key])



"""
class Services(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.Integer)
    update_date = db.Column(db.Date)
    start_date = db.Column(db.Date)
    stop_date = db.Column(db.Date)
    message = db.Column(db.String(500))

    def __init__(self, name, status, update_date, start_date, stop_date, message):
        self.name = name
        self.status = status
        self.update_date = update_date
        self.start_date = start_date
        self.stop_date = stop_date
        self.message = message

    def __repr__(self):
        return '<Service %r, status %r>' % self.name, self.status

class Events(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    update_date = db.Column(db.Date)
    message = db.Column(db.String(500))

    def __init__(self, name, status, update_date, start_date, stop_date, message):
        self.name = name
        self.status = status
        self.update_date = update_date
        self.start_date = start_date
        self.stop_date = stop_date
        self.message = message

    def __repr__(self):
        return '<Service %r, status %r>' % self.name, self.status
"""