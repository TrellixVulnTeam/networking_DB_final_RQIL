# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20180114_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beenrestaurant',
            old_name='been',
            new_name='times',
        ),
    ]
