
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
router = DefaultRouter()
router.register(r'singer', views.SingerViewSet,basename="singer")
router.register(r'song', views.SongViewSet,basename="song")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    
    
]
