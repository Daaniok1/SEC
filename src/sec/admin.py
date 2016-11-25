from import_export import resources
from django.contrib import admin
from sec.models import *

class asignaturaAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'eje', 'nivel' , 'creditos', 'disponible')
	list_filter = ('eje', 'creditos', 'disponible',)

class contenidoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'asignatura' ,'status')
	list_filter = ('asignatura' ,'status',)

class preguntaAdmin(admin.ModelAdmin):
	list_display = ('id_pregunta', 'tipo_pregunta', 'status', 'created_at', 'updated_at')
	list_filter = ('tipo_pregunta', 'dificultad', 'asignatura' ,'status',)


class evaluacionAdmin(admin.ModelAdmin):
	list_display = ('id_evaluacion', 'tipoEvaluacion', 'asignatura' ,'status', 'created_at', 'updated_at')
	list_filter = ('tipoEvaluacion', 'asignatura','status', )


admin.site.register(asignatura, asignaturaAdmin)
admin.site.register(contenido, contenidoAdmin)
admin.site.register(pregunta, preguntaAdmin)
admin.site.register(evaluacion, evaluacionAdmin)