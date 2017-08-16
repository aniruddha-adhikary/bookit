from django.apps import apps
from django.conf import settings
from django.db import models

from bookings.models import Booking


class ProviderManager(models.Manager):
    pass


class Provider(models.Model):

    name = models.CharField(
        max_length=140
    )

    area = models.ForeignKey(
        to='geo.Area'
    )

    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    objects = ProviderManager()

    def get_bookings(self):
        return Booking.objects.filter(service__provider=self)
