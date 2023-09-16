from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class TestsPagination(PageNumberPagination):
    page_size = settings.NUM_OBJECTS_ON_PAGE
