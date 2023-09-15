from rest_framework.permissions import IsAuthenticated

from api.mixins import ListRetrieveAPIView
from api.serializers import TestsSerializer
from researches.models import Test


class TestsAPIView(ListRetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestsSerializer
    permission_classes = (IsAuthenticated,)
