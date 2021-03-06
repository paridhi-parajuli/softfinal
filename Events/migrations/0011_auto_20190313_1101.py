# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-13 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0010_remove_event_total_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='contact',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_organizers',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_rooms',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'lecture 1'), (2, 'lecture2'), (3, 'lecture3'), (4, 'lecture4')], max_length=7),
        ),
    ]
