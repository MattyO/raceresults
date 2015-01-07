# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20141007_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raceresult',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='race',
            name='course',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='length',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True),
        ),
    ]
