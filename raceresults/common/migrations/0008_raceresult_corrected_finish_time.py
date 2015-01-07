# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20150107_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='raceresult',
            name='corrected_finish_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
