import django_filters
from .models import Ad


# Фильтры в Django базируются на основе моделей


class AdFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )

    class Meta:
        model = Ad
        fields = ("title",)
