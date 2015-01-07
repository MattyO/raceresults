# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20150107_0629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='raceresult',
            options={'ordering': ['finish_place']},
        ),
        migrations.AddField(
            model_name='raceresult',
            name='finish_place',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
