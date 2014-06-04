#!/usr/bin/python
from canary.database import meta
from sqlalchemy import MetaData

meta.reflect()
meta.drop_all()
