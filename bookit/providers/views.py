from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django_filters.views import FilterView

from providers.filtersets import ProviderServiceFilterSet
from providers.forms import ProviderForm, ProviderServiceForm
from providers.models import Provider, ProviderService


### Provider Service View ###


class ProviderServiceFilterView(FilterView):
    model = ProviderService
    filterset_class = ProviderServiceFilterSet

    def get_queryset(self):
        return ProviderService.objects.all().select_related('provider')


class ProviderServiceListView(generic.ListView):
    model = ProviderService
    filterset_class = ProviderServiceFilterSet

    def get_queryset(self):
        return ProviderService.objects.filter(provider=Provider.objects.get(pk=self.kwargs.get('pk'))).order_by('id')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pk'] = self.kwargs['pk']
        return ctx


class ProviderServiceCreateView(LoginRequiredMixin, generic.CreateView):
    model = ProviderService
    form_class = ProviderServiceForm

    def get_success_url(self):
        return reverse('providerservice-list', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        retval = super().post(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, "The service has been added successfully",
                             'alert alert-success')
        return retval

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['provider'] = get_object_or_404(Provider, pk=self.kwargs['pk'])
        return kwargs


class ProviderServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = ProviderService
    form_class = ProviderServiceForm

    def test_func(self):
        return self.request.user == self.get_object().provider.owner

    def get_success_url(self):
        return reverse('providerservice-list', kwargs={'pk': self.kwargs['provider_pk']})

    def post(self, request, *args, **kwargs):
        retval = super().post(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, "The service has been updated successfully",
                             'alert alert-success')
        return retval

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['provider'] = get_object_or_404(Provider, pk=self.kwargs['provider_pk'])
        return kwargs


class ProviderServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = ProviderService

    def test_func(self):
        return self.request.user == self.get_object().provider.owner

    def get_success_url(self):
        return reverse('providerservice-list', kwargs={'pk': self.kwargs['provider_pk']})

    def post(self, request, *args, **kwargs):
        retval = super().post(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, "The service has been deleted successfully",
                             'alert alert-success')
        return retval


### Provider Views ###



class ProviderListView(LoginRequiredMixin, generic.ListView):
    model = Provider

    def get_queryset(self):
        return Provider.objects.filter(owner=self.request.user)


class ProviderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Provider
    form_class = ProviderForm

    def get_success_url(self):
        return reverse('provider-list-user')

    def post(self, request, *args, **kwargs):
        retval = super().post(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, "The company has been added successfully",
                             'alert alert-success')
        return retval

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class ProviderUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Provider
    form_class = ProviderForm

    def get_success_url(self):
        return reverse('provider-list-user')

    def test_func(self):
        return self.request.user == self.get_object().owner

    def post(self, request, *args, **kwargs):
        retval = super().post(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, "The company has been updated successfully",
                             'alert alert-success')
        return retval

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs
