from rest_framework.pagination import CursorPagination

# class MyPagination(PageNumberPagination):
#   page_size = 3
#   page_query_params = 'p'
#   page_query_param = 'records'
#   max_page_size=7
#   last_page_strings='end'

class MyPagination(CursorPagination):
  page_size=2
  cursor_query_param='cursor'
  ordering='roll'