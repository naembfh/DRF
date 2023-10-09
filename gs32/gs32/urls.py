from api.views import StudentList, StudentCreate, StudentRetrieve, StudentUpdate, StudentDestroy
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', StudentList.as_view(), name='student-list'),  
    # path('studentapi/', StudentCreate.as_view(), name='student-create'), 
    # path('studentapi/<int:pk>/', StudentRetrieve.as_view(), name='student-retrieve'),  
    # path('studentapi/<int:pk>/update/', StudentUpdate.as_view(), name='student-update'),  
    path('studentapi/<int:pk>/', StudentDestroy.as_view(), name='student-destroy'),
]
