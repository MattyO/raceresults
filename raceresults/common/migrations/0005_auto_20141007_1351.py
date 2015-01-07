# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20140909_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='race',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='series',
            name='owner',
        ),
    ]
