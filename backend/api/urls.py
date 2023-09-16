from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from api.views import TestsAPIView

v1_router = routers.DefaultRouter()
v1_router.register('tests', TestsAPIView, basename='tests')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'v1/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
]
