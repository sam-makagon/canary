from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, text

Base = declarative_base()

class Service(Base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    user = Column(String(30), nullable=False)
    host = Column(String(30), nullable=False)
    status = Column(Integer, ForeignKey('status.id'))
    modify_date = Column(DateTime, index=True, server_default=text('CURRENT_TIMESTAMP'))
    start_date = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    stop_date = Column(DateTime)
    message = Column(String(1000), index=True)
    arguments = Column(String(1000), index=True)

    def __init__(self, name, user, host, status, modify_date=None, start_date=None, stop_date=None, message=None, arguments=None):
        self.name = name
        self.user = user
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
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('service.id'), index=True)
    user = Column(String(30), nullable=False)
    host = Column(String(30), nullable=False)
    event = Column(Integer, ForeignKey('event_defn.id'))
    status = Column(Integer, ForeignKey('status.id'))
    modify_date = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    message = Column(String(1000), index=True)
    arguments = Column(String(1000), index=True)

    def __init__(self, parent_id, user, host, event, status, modify_date=None, message=None, arguments=None):
        self.parent_id = parent_id
        self.user = user
        self.host = host
        self.event = event
        self.status = status
        self.modify_date = modify_date
        self.message = message
        self.arguments = arguments

    def __repr__(self):
        return '<Service %r, status %r, date %r>' % (self.id, self.status, self.modify_date)

class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, autoincrement=False)
    status_description = Column(String(10), unique=True)

    def __init__(self, id, status_description):
        self.id = id
        self.status_description = status_description

    def __repr__(self):
        return '<status_description %r>' % self.status_description

class EventDefn(Base):
    __tablename__ = 'event_defn'

    id = Column(Integer, primary_key=True, autoincrement=False)
    event_description = Column(String(10), unique=True)

    def __init__(self, id, event_description):
        self.id = id
        self.event_description = event_description

    def __repr__(self):
        return '<event_description %r>' % self.event_description

