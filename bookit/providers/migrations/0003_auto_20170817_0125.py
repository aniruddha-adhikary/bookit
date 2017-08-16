# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-16 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_provider_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='map_query',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='providerservice',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='providers.Provider'),
        ),
    ]