from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_fsm import FSMField
from model_utils import Choices


class Booking(models.Model):
    STATES = Choices(
        ('REQUESTED', 'requested', _('Requested')),
        ('APPROVED',  'approved',  _('Approved')),
        ('REJECTED',  'rejected',  _('Rejected')),
        ('CANCELLED', 'cancelled', _('Cancelled'))
    )

    service = models.ForeignKey(
        to='providers.ProviderService'
    )

    status = FSMField(
        default=STATES.requested
    )

    booked_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL
    )

    booked_for = models.DateTimeField()

    booked_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )
