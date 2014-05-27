import math
from decimal import Decimal

ITEMS_PER_PAGE = 50

def get_total_pages(record_count):
  return int(math.ceil(Decimal(record_count / ITEMS_PER_PAGE )))

def get_offset(cur_page):
  return (cur_page-1) * ITEMS_PER_PAGE

