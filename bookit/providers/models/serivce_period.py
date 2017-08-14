from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices


class ServicePeriod(models.Model):
    DAYS_OF_WEEK = Choices(
        ('SATURDAY', 'saturday', _('Saturday')),
        ('SUNDAY', 'sunday', _('Sunday')),
        ('MONDAY', 'monday', _('Monday')),
        ('TUESDAY', 'tuesday', _('Tuesday')),
        ('WEDNESDAY', 'wednesday', _('Wednesday')),
        ('THURSDAY', 'thursday', _('Thursday')),
        ('FRIDAY', 'friday', _('Friday'))
    )

    provider = models.ForeignKey(
        to='providers.Provider'
    )

    day_of_week = models.CharField(
        max_length=9,
        unique=True,
    )

    opens_at = models.TimeField()
    closes_at = models.TimeField()
