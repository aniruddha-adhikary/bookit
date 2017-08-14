from django.db import models


class ProviderService(models.Model):
    name = models.CharField(
        max_length=140
    )

    short_description = models.CharField(
        max_length=200
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    time_required = models.DurationField()

    provider = models.ForeignKey(
        to='providers.Provider'
    )
