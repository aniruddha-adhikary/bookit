from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class PhoneNumber(models.Model):

    provider = models.ForeignKey(
        to='providers.Provider'
    )

    phone_number = PhoneNumberField()
