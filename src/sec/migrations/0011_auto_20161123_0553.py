# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-23 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0010_pregunta_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
