from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, text

"""
statusTable = Table('statuses', metadata, autoload=True)
serviceTable = Table('services', metadata, autoload=True)
eventTable = Table('events', metadata, autoload=True)

statuses = {}
for (status_id, name) in session.query(statusTable).all():
    statuses[status_id] = name
"""

Base = declarative_base()

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    host = Column(String(20), nullable=False)
    status = Column(Integer, ForeignKey('statuses.id'))
    modify_date = Column(DateTime, index=True, server_default=text('GETDATE()'))
    start_date = Column(DateTime, server_default=text('GETDATE()'))
    stop_date = Column(DateTime)
    message = Column(String(1000), index=True)
    arguments = Column(String(1000), index=True)

    def __init__(self, name, host, status, modify_date, start_date, stop_date, message, arguments):
        self.name = name
        self.host = host
        self.status = status
        self.modify_date = modify_date
        self.start_date = start_date
        self.stop_date = stop_date
        self.message = message
        self.arguments = arguments

    def __repr__(self):
        return '<Name %r, status %r>' % (self.name, self.status)

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('services.id'), index=True)
    host = Column(String(20), nullable=False)
    status = Column(Integer, ForeignKey('statuses.id'))
    modify_date = Column(DateTime, server_default=text('GETDATE()'))
    message = Column(String(1000), index=True)
    arguments = Column(String(1000), index=True)

    def __init__(self, parent_id, host, status, modify_date, message, arguments):
        self.parent_id = parent_id
        self.host = host
        self.status = status
        self.modify_date = modify_date
        self.message = message
        self.arguments = arguments

    def __repr__(self):
        return '<Service %r, status %r, date %r>' % (self.id, self.status, self.modify_date)

class Status(Base):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True, autoincrement=False)
    description = Column(String(10), unique=True)

    def __init__(self, id, description):
        self.id = id
        self.description = description

    def __repr__(self):
        return '<description %r>' % self.description

