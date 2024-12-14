from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
  page_size = 3
  page_query_params = 'p'
  page_query_param = 'records'
  max_page_size=7
  last_page_strings='end'