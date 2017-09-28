# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-18 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='all_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='word',
            name='correct_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]