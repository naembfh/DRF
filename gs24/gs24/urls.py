
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from django.contrib import admin
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'studentapi', views.StudentModelViewSet,basename="student")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework'))
]