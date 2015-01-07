# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_raceresult_corrected_finish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raceresult',
            name='corrected_finish_time',
            field=models.DateTimeField(null=True, editable=False, blank=True),
        ),
    ]
