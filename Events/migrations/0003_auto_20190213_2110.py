# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-13 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20190213_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_organizers',
            field=models.TextField(default=0),
        ),
    ]