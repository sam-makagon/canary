#!/usr/bin/python
import canary
from canary.database import engine, session
from canary.models import Base, Status, EventDefn

Base.metadata.create_all(engine)

session.add(Status(0, 'SUCCESS'))
session.add(Status(1, 'WARNING'))
session.add(Status(2, 'ERROR'))
session.add(Status(3, 'RUNNING'))

session.add(EventDefn(0, 'START'))
session.add(EventDefn(1, 'STOP'))
session.add(EventDefn(2, 'INFO'))

session.commit()
