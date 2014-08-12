#!/usr/bin/python
import canary
from canary.database import engine, session
from canary.models import Base, Status, EventDefn

session.execute("""
update service 
set message = null
where message is not null
and id not in (
	select distinct s.id
	from service s join event e on s.id = e.parent_id and s.message = e.message
	where  s.message is not null
	and e.modify_date > dateadd(day,datediff(day,1,GETDATE()),0)
)
""")

session.commit()
