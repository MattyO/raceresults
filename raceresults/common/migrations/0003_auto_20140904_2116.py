# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20140904_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
