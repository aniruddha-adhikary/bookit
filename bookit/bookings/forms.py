from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.admin import widgets

from bookings.models import Booking
from providers.models import ProviderService


class CreateBookingForm(forms.ModelForm):
    booked_for = forms.DateTimeField()

    class Meta:
        model = Booking
        fields = ('booked_for',)

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        self._service = kwargs.pop('service')
        super().__init__(*args, **kwargs)
        self.fields['booked_for'].widget.attrs['placeholder'] = 'Appointment Time* '
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        # self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Create Booking'))

    def save(self, commit=True):
        self.instance.booked_by = self._user
        self.instance.service = self._service
        return super().save(commit)


