from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from api.mixins import ListRetrieveAPIView
from api.serializers import TestsSerializer
from core.paginations import TestsPagination
from researches.models import Test


class TestsAPIView(ListRetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestsSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = TestsPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('lab',)
    search_fields = ('^id',)
