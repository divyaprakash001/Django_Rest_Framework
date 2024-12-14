from rest_framework.pagination import LimitOffsetPagination

# class MyPagination(PageNumberPagination):
#   page_size = 3
#   page_query_params = 'p'
#   page_query_param = 'records'
#   max_page_size=7
#   last_page_strings='end'

class MyPagination(LimitOffsetPagination):
  default_limit=2
  limit_query_param='upto'
  offset_query_param="chhoro"
  max_limit=4