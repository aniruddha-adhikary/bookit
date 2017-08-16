from django.forms import Form
from django_filters import filters
from django_filters.filterset import FilterSet

from geo.models import Area
from providers.forms import SearchForm
from providers.models import ProviderService


class ProviderServiceFilterSet(FilterSet):

    name = filters.CharFilter(
        lookup_expr='icontains'
    )

    area = filters.ModelChoiceFilter(
        name='provider__area',
        lookup_expr='exact',
        queryset=Area.objects.all()
    )

    class Meta:
        model = ProviderService
        form = SearchForm
        fields = []
