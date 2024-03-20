from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .apps import SalesConfig
from .views import AdViewSet, AdMyListAPIView, CommentViewSet

app_name = SalesConfig.name

ad_router = DefaultRouter()
ad_router.register(r'ads', AdViewSet, basename='объявление')

com_router = NestedDefaultRouter(ad_router, r'ads', lookup='ad')
com_router.register(r'comments', CommentViewSet, basename='комментарий')

urlpatterns = [
    path('ads/me/', AdMyListAPIView.as_view(), name='мои объявления')
              ]
urlpatterns += ad_router.urls
urlpatterns += com_router.urls
