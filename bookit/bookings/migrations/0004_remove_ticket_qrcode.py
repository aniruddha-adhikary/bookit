# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-16 19:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20170817_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='qrcode',
        ),
    ]