# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-21 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('requisito', models.CharField(max_length=50, null=True)),
                ('corequisito', models.CharField(max_length=50, null=True)),
                ('regimen', models.IntegerField(choices=[(1, b'Diurno'), (2, b'Vespertino'), (3, b'Advance')], default=1)),
                ('eje', models.IntegerField(choices=[(1, b'Gesti\xc3\xb3n de proyectos'), (2, b'Arquitectura de software'), (3, b'Desarrollo de software'), (4, b'Comunicaci\xc3\xb3n en ingles'), (5, b'Educaci\xc3\xb3n general'), (6, b'Vinculaci\xc3\xb3n con el medio')])),
                ('caracter', models.CharField(max_length=30, null=True)),
                ('nivel', models.IntegerField(choices=[(1, b'1er Semestre'), (2, b'2do Semestre'), (3, b'3er Semestre'), (4, b'4to Semestre'), (5, b'5to Semestre'), (6, b'6to Semestre'), (7, b'7mo Semestre'), (8, b'8vo Semestre')], default=1)),
                ('duracion', models.CharField(max_length=15, null=True)),
                ('creditos', models.IntegerField(default=1)),
                ('horas_teoricas', models.IntegerField(default=1)),
                ('horas_practicas', models.IntegerField(blank=True, null=True)),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_contenido', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True)),
                ('objetivos_aprendizaje', models.TextField(null=True)),
                ('status', models.BooleanField()),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sec.asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_evaluacion', models.CharField(max_length=50)),
                ('objetivos_a_medir', models.TextField(null=True)),
                ('tipoEvaluacion', models.IntegerField(choices=[(1, b'Solemne'), (2, b'Control'), (3, b'Examen'), (4, b'Quizz')], default=1)),
                ('cant_preguntas', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField()),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sec.asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pregunta', models.CharField(max_length=50)),
                ('tipo_pregunta', models.IntegerField(choices=[(1, b'Desarrollo'), (2, b'Seleccion m\xc3\xbaltiple'), (3, b'T\xc3\xa9rminos pareados')], default=1)),
                ('dificultad', models.IntegerField(choices=[(1, b'Bajo (10% - 30%)'), (2, b'Medio (30% - 60%)'), (3, b'Alto (60% - 90%')], default=1)),
                ('pregunta', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/data')),
                ('respuesta', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField()),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sec.asignatura')),
                ('contenido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sec.contenido')),
            ],
        ),
    ]
