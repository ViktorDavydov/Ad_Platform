from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apps import SalesConfig
from .views import AdViewSet, AdListAPIView

app_name = SalesConfig.name
router = DefaultRouter()

router.register(r'ads', AdViewSet, basename='объявление')

urlpatterns = [
    path('ads/me/', AdListAPIView.as_view(), name='мои объявления')
              ] + router.urls
