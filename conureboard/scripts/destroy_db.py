from conureboard.database import meta
from sqlalchemy import MetaData

meta.reflect()
meta.drop_all()
