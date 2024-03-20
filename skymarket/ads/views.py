from rest_framework import pagination, viewsets, generics

from .models import Ad
from .serializers import AdSerializer, AdListSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ["retrieve", "preform_create", "update"]:
            return AdListSerializer
        else:
            return AdSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdMyListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    pass
