from __future__ import division
import math
from conureboard.config import ITEMS_PER_PAGE

def get_total_pages(record_count):
  return int(math.ceil(record_count / ITEMS_PER_PAGE))

def get_offset(cur_page):
  return (cur_page-1) * ITEMS_PER_PAGE

