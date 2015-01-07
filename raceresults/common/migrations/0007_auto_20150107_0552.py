# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20150107_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raceresult',
            name='finish_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
