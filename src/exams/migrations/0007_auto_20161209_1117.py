# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_response_is_last'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='rating',
        ),
        migrations.AddField(
            model_name='response',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]