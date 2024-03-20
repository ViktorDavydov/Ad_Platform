from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets, generics

from .filters import AdFilter
from .models import Ad, Comment
from .serializers import AdSerializer, AdListSerializer, CommentListSerializer, CommentCreateSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "retrieve":
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
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "create":
            return CommentCreateSerializer
        return CommentListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad_id=self.kwargs['ad_pk'])

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_pk'])
