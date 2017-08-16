from django.views import generic
from django_filters.views import FilterView

from providers.filtersets import ProviderServiceFilterSet
from providers.models import Provider, ProviderService


class ProviderServiceListView(FilterView):
    model = ProviderService
    filterset_class = ProviderServiceFilterSet
    template_name = 'providers/providerservice_filter.html'

    def get_queryset(self):
        return ProviderService.objects.all().select_related('provider')


