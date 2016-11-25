#!/usr/bin/env python
# Este archivo usa el encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from sec.choices import *

class asignatura(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    requisito = models.CharField(max_length=50, blank=True, null=True)
    corequisito = models.CharField(max_length=50, null=True)
    regimen = models.IntegerField(choices = regimenAsignatura, default=1)
    eje = models.IntegerField(choices = ejesAsignatura)
    caracter = models.CharField(max_length=30, null=True)
    nivel = models.IntegerField(choices = nivelAsignatura, default=1)
    objetivos = models.TextField(null=True)
    duracion = models.CharField(max_length=15, null=True)
    creditos = models.IntegerField()
    horas_teoricas = models.IntegerField()
    horas_practicas = models.IntegerField(blank=True, null=True)
    disponible = models.BooleanField()

    def __str__(self):
        return self.nombre


class contenido(models.Model):
    id_contenido = models.CharField(max_length=10)
    asignatura = models.ForeignKey(asignatura, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)
    objetivos_aprendizaje = models.TextField(null=True)
    status = models.BooleanField()

    def __str__(self):
        return self.nombre

class pregunta(models.Model):
    id_pregunta = models.CharField(max_length=50)
    asignatura = models.ForeignKey(asignatura, null=True, blank=True, on_delete=models.CASCADE)
    contenido = models.ForeignKey(contenido, null=True, blank=True, on_delete=models.CASCADE)
    tipo_pregunta = models.IntegerField(choices = tipoPregunta, default=1)
    dificultad = models.IntegerField(choices = dificultadPregunta, default=1)
    pregunta = models.TextField()
    imagen = models.ImageField(upload_to='images/data', blank=True, null=True)
    respuesta = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.id_pregunta


class evaluacion(models.Model):
    id_evaluacion = models.CharField(max_length=50)
    asignatura = models.ForeignKey(asignatura, null=True, blank=True, on_delete=models.CASCADE)
    objetivos_a_medir = models.TextField(null=True)
    tipoEvaluacion = models.IntegerField(choices = tipoEvaluacion, default=1)
    preguntas = models.ManyToManyField(pregunta,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    def __str__(self):
        return self.id_evaluacion