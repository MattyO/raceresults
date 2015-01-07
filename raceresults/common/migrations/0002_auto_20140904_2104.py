# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='type',
            field=models.ForeignKey(blank=True, to='common.BoatType', null=True),
        ),
    ]
