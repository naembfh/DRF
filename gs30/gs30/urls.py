
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)


router = DefaultRouter()
router.register(r'studentapi', views.StudentModelViewSet,basename="student")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify')
  
]