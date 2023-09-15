from rest_framework import mixins, viewsets


class ListRetrieveAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pass
