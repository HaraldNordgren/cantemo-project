# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 01:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_bank', '0002_auto_20160413_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankimage',
            name='file_format',
        ),
    ]
