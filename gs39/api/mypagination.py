from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit= 5
    
    
    #http://127.0.0.1:8000/studentapi/?limit=6