from flask import Flask
from pyodbc import *

#from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql.functions import current_date

from conureboard import app
from conureboard.config import DB_ENGINE

engine = create_engine(DB_ENGINE)
meta = MetaData(bind=engine)
Session = sessionmaker(bind=engine)
session = scoped_session(Session)

def printquery(statement, bind=None):
  """
  print a query, with values filled in
  for debugging purposes *only*
  for security, you should always separate queries from their values
  please also note that this function is quite slow
  """
  import sqlalchemy.orm
  if isinstance(statement, sqlalchemy.orm.Query):
      if bind is None:
          bind = statement.session.get_bind(
                  statement._mapper_zero_or_none()
          )
      statement = statement.statement
  elif bind is None:
      bind = statement.bind 

  dialect = bind.dialect
  compiler = statement._compiler(dialect)
  class LiteralCompiler(compiler.__class__):
      def visit_bindparam(
              self, bindparam, within_columns_clause=False, 
              literal_binds=False, **kwargs
      ):
          return super(LiteralCompiler, self).render_literal_bindparam(
                  bindparam, within_columns_clause=within_columns_clause,
                  literal_binds=literal_binds, **kwargs
          )

  compiler = LiteralCompiler(dialect, statement)
  print compiler.process(statement)
