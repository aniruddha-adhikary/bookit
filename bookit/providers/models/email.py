from django.db import models


class EmailAddress(models.Model):

    provider = models.ForeignKey(
        to='providers.Provider'
    )

    email_address = models.EmailField()
