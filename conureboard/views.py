import sys
from flask import render_template, request

from conureboard import app, models
from conureboard.database import session, printquery
from conureboard.paginate import get_total_pages, get_offset, ITEMS_PER_PAGE

DEBUG = 0

@app.route('/')
@app.route('/conureboard/')
def show_services():
  cur_page = get_page(request)
  offset = get_offset(cur_page)

  if DEBUG:
    logmsg("offset=%s, limit=%s" % (offset, ITEMS_PER_PAGE))

  #base services query
  services = session.query(models.Service).\
              join(models.Status).\
              with_entities(models.Service.id, models.Service.name, models.Service.host, models.Service.status, models.Service.modify_date, models.Service.start_date,\
                models.Service.stop_date, models.Service.message, models.Service.arguments, models.Status.description )
  
  #apply search
  if request.args.get('search'):
    search_term = '%%%s%%' % request.args.get('search')
    services = services.filter( (models.Service.message.like(search_term)) | (models.Service.name.like(search_term)) )

  #apply sort
  if request.args.get('sort_by'):
    if request.args.get('sort_order') == 'desc':
      services = services.order_by(getattr(models.Service, request.args.get('sort_by')).desc())
    else:
      services = services.order_by(models.Service.modify_date.desc())
  else:
    #default sort
    services = services.order_by(models.Service.modify_date.desc())


  #apply offset and limit
  services = services.offset(offset).limit(ITEMS_PER_PAGE)

  if DEBUG:
    logmsg(printquery(services))

  rowcount = session.query(models.Service.id).count()
  total_pages = get_total_pages(rowcount)

  logmsg("rendering template")
  return render_template('services.html', rowcount=rowcount, items=services, statuses=models.Status, \
    total_pages=total_pages, cur_page=cur_page, offset=offset, request=request)



@app.route('/services/<int:service_id>')
@app.route('/conureboard/services/<int:service_id>')
def show_events(service_id):
  cur_page = get_page(request)
  offset = get_offset(cur_page)
  rowcount = session.query(models.Event).filter(models.Event.parent_id == service_id).count()
  total_pages = get_total_pages(rowcount)

  if DEBUG:
    logmsg("offset=%s, limit=%s, rowcount=%s, cur_page=%s, total_pages=%s, search=%s" % (offset, ITEMS_PER_PAGE, rowcount, cur_page, \
      total_pages, request.args.get('search')))

  #base event query
  events = session.query(models.Event).\
            join(models.Service).\
            join(models.Status, models.Status.id == models.Event.status).\
            filter(models.Service.id == service_id).\
            order_by(models.Event.modify_date.desc()).\
            with_entities( models.Service.name, models.Status.description, models.Event.status, models.Event.modify_date,\
              models.Event.message )
  
  #apply search
  if request.args.get('search'):
    search_term = '%%%s%%' % request.args.get('search')
    events = events.filter(models.Event.message.like(search_term) )

  #apply offset and limit
  events = events.offset(offset).limit(ITEMS_PER_PAGE)

  if DEBUG:
    logmsg(printquery(events))

  return render_template('events.html', rowcount=rowcount, items=events, statuses=models.Status, \
   total_pages=total_pages, request=request, cur_page=cur_page, offset=offset)

def get_page(request):
  page = request.args.get('page')
  page_num = None
  if page != None:
    try:
      page_num = int(page)
    except ValueError:
      page_num = 1
  else:
    page_num = 1

  return page_num

def logmsg(msg):
  print >> sys.stderr, msg
