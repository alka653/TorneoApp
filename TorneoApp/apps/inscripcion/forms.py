# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class InscripcionForm(forms.ModelForm):
	class Meta:
		model = Inscritos
		fields = '__all__'
		exclude = ('date_registry', )
		labels = {
			'fullname': 'Nombres completos',
			'email': 'Correo electrónico',
			'nivel': 'Nivel de juego'
		}

	def __init__(self, *args, **kwargs):
		super(InscripcionForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control', 'required': True})