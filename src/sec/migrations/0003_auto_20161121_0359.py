# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-21 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0002_auto_20161121_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='creditos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='horas_teoricas',
            field=models.IntegerField(),
        ),
    ]
