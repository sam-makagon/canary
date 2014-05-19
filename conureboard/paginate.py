import math
from decimal import Decimal

def get_page_info(record_count, page, items_per_page):
  return get_page_number(record_count, page, items_per_page), get_total_pages(record_count, items_per_page)

def get_page_number(record_count, page, items_per_page):
  num_pages = record_count / items_per_page
  return (page / items_per_page) + 1

def get_total_pages(record_count, items_per_page):
  return int(math.ceil(Decimal(record_count / items_per_page)))
