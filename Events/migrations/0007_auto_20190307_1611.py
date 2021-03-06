# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-07 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_auto_20190216_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(verbose_name='event date'),
        ),
    ]
