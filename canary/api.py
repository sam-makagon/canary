import flask.ext.restless

from canary import app, models, logmsg, EVENT_START, EVENT_STOP
from canary.database import session, printquery
from canary.paginate import get_total_pages, get_offset
from canary.config import ITEMS_PER_PAGE, DEBUG
from canary import app, models
from canary.database import session


# update service based on new event
def update_service(data=None, **kw):
  if DEBUG:
    logmsg("data=%s, kw=%s" % (data, kw)) 

  update = {'status': kw['result']['status']}
  update['modify_date'] = kw['result']['modify_date']
  
  if kw['result']['message']: 
    update['message'] = kw['result']['message']
  
  if kw['result']['event'] == EVENT_START:
    update['start_date'] = kw['result']['modify_date']
  elif kw['result']['event'] == EVENT_STOP:
    update['stop_date'] = kw['result']['modify_date']

  if kw['result']['arguments']:
    update['arguments'] = kw['result']['arguments']

  try:
    session.query(models.Service).filter(models.Service.id == kw['result']['parent_id']).update(update)
    session.commit()
  except Exception as e:
    logmsg("exception caught updating service %s" % e)

manager = flask.ext.restless.APIManager(app, session=session)
service_blueprint = manager.create_api(models.Service, methods=['GET', 'POST'])
service_blueprint = manager.create_api(models.Event, 
    methods=['GET', 'POST'],
    postprocessors={
      'POST' : [update_service]
    }
)
