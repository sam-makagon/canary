from flask import render_template, request
from pprint import pprint

from conureboard import app
from conureboard.database import model, session
from conureboard.model import statuses
from conureboard.paginate import get_page_info

items_per_page = 2

@app.route('/')
def show_services():
	cur_page = 1
	if request.args.get('page') != None:
		cur_page = int(request.args.get('page'))
	
	rowcount = session.query(model.serviceTable.c.id).count()
	offset = (cur_page-1)*items_per_page

	print "offset=%s, limit=%s" % (offset, items_per_page)

	services = session.query(model.serviceTable).\
							order_by(model.serviceTable.c.modifyDt.desc()).\
							offset(offset).\
							limit(items_per_page)
  
	print printquery(services)
	
	(page_num, total_pages) = get_page_info(rowcount, cur_page, items_per_page)

	print services
	return render_template('services.html', rowcount=rowcount, items=services, statuses=statuses, page_num=page_num, total_pages=total_pages)

@app.route('/events/<int:service_id>')
def show_events(service_id):
	rowcount = session.query(model.eventTable).filter(model.eventTable.c.id == service_id).count()
	events = session.query(model.eventTable, model.serviceTable).\
						join(model.serviceTable, model.eventTable.c.id == model.serviceTable.c.id).\
						filter(model.eventTable.c.id == service_id).\
						order_by(model.eventTable.c.modifyDt.desc()).\
						with_entities(model.serviceTable.c.name, model.eventTable.c.status, model.eventTable.c.modifyDt, model.eventTable.c.message ).\
						offset((cur_page-1)*items_per_page).\
						limit(items_per_page)
	print events
	pprint (vars(events))
	return render_template('events.html', rowcount=rowcount, items=events, statuses=statuses)


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
