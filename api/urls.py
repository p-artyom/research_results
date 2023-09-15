from django.urls import include, path
from rest_framework import routers

from api.views import TestsAPIView

v1_router = routers.DefaultRouter()
v1_router.register('tests', TestsAPIView, basename='tests')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
