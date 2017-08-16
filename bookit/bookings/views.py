from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from bookings.forms import CreateBookingForm
from bookings.models import Booking
from providers.models import ProviderService, Provider


class BookingListViewCustomer(LoginRequiredMixin, generic.ListView):
    model = Booking

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(booked_by=user).select_related('service', 'service__provider')


class AllBookingListViewForProvider(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Booking
    template_name = 'bookings/booking_list_provider.html'

    def test_func(self):
        return self.request.user == get_object_or_404(Provider, pk=self.kwargs['pk']).owner

    def get_queryset(self):
        return Booking.objects.filter(service__provider=get_object_or_404(Provider, pk=self.kwargs['pk']))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['provider'] = get_object_or_404(Provider, pk=self.kwargs['pk'])
        return ctx


class CreateBookingView(LoginRequiredMixin, generic.CreateView):
    model = Booking
    form_class = CreateBookingForm
    success_url = '/search'
    template_name = 'bookings/booking_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['service'] = get_object_or_404(ProviderService, pk=self.kwargs['pk'])
        return kwargs

    def form_valid(self, form):
        resp = super().form_valid(form)

        messages.add_message(self.request,
                             messages.SUCCESS,
                             "Your booking has been sent for approval",
                             extra_tags='alert alert-success')

        return resp

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['service'] = get_object_or_404(ProviderService, pk=self.kwargs['pk'])
        return ctx



class BookingStateChangeView(LoginRequiredMixin, generic.RedirectView):
    state_change_method: str = None
    reverse: str = 'booking-list'

    @property
    def reverse_kwargs(self):
        return {}

    def get_redirect_url(self, *args, **kwargs):

        obj = get_object_or_404(Booking, pk=self.kwargs['pk'])

        self.obj = obj

        try:
            getattr(obj, self.state_change_method)()
            obj.save()
        except:
            messages.add_message(
                self.request,
                messages.ERROR,
                extra_tags='alert alert-error',
                message='Unable to process your request.'
            )

        return reverse(self.reverse, kwargs=self.reverse_kwargs)


class BookingCancelView(BookingStateChangeView):
    state_change_method = 'cancel'


class BookingApproveView(BookingStateChangeView):
    state_change_method = 'approve'
    reverse = 'booking-list-provider'

    @property
    def reverse_kwargs(self):
        return {'pk': self.obj.service.provider_id}


class BookingRejectView(BookingStateChangeView):
    state_change_method = 'reject'
    reverse = 'booking-list-provider'

    @property
    def reverse_kwargs(self):
        return {'pk': self.obj.service.provider_id}
