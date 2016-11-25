from django import forms 
from sec.models import *

class preguntaForm(forms.ModelForm):

	class Meta:
		model = pregunta

		fields = [
			'id_pregunta',
			'asignatura',
			'contenido',
			'tipo_pregunta',
			'dificultad',
			'pregunta',
			'imagen',
			'respuesta',
		]

		labels = {
			'id_pregunta': 'Codigo',
			'asignatura': 'Asignatura' ,
			'contenido': 'Contenido' ,
			'tipo_pregunta': 'Tipo de pregunta' ,
			'dificultad': 'Dificultad aproximada' ,
			'pregunta': 'Pregunta' ,
			'imagen': 'Imagen' ,
			'respuesta': 'Respuesta' ,
		}

		widgets = {
			'id_pregunta': forms.TextInput(attrs={'class': 'form-group'}),
			'asignatura': forms.Select(attrs={'class': 'form-group'}),
			'contenido': forms.Select(attrs={'class': 'form-group'}),
			'tipo_pregunta': forms.Select(attrs={'class': 'form-group'}),
			'dificultad': forms.Select(attrs={'class': 'form-group'}),
			'pregunta': forms.Textarea(attrs={'class': 'form-group'}),
			'imagen': forms.Select(attrs={'class': 'form-group'}),
			'respuesta': forms.Textarea(attrs={'class': 'form-group'}),
			'status': forms.RadioSelect(),
		}