from django.db import models


class Provider(models.Model):

    name = models.CharField(
        max_length=140
    )

    area = models.ForeignKey(
        to='geo.Area'
    )
