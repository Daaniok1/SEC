# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-23 05:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0008_auto_20161122_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='imagen',
        ),
    ]
