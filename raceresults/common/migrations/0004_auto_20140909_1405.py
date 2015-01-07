# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20140904_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('finish_time', models.DateTimeField()),
                ('boat', models.ForeignKey(to='common.Boat')),
                ('race', models.ForeignKey(to='common.Race')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='result',
            name='boat',
        ),
        migrations.RemoveField(
            model_name='result',
            name='race',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
