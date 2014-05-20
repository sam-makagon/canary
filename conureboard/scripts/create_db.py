import conureboard
from conureboard.database import engine, session
from conureboard.models import Base, Status

Base.metadata.create_all(engine)

status = Status(1, 'SUCCESS')
session.add(status)
status = Status(2, 'WARNING')
session.add(status)
status = Status(3, 'ERROR')
session.add(status)
status = Status(4, 'RUNNING')
session.add(status)
session.commit()
