# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-17 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20161117_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='figure',
            field=models.CharField(default='none', max_length=100),
        ),
    ]