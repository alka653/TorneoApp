# -*- encoding: utf-8 -*-
from mail_templated import send_mail
from django.conf import settings
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
			'telefono': 'Número telefónico',
			'email': 'Correo electrónico',
			'nivel': 'Nivel de juego'
		}

	def save(self):
		save_data = super(InscripcionForm, self).save()
		data = {
			'subject': 'Torneo de ajedrez 2017 UPC',
			'args': {
				'fullname': save_data.fullname,
				'telefono': save_data.telefono,
				'email': save_data.email
			}
		}
		send_mail('email/send_email.html', data, settings.DEFAULT_FROM_EMAIL, [save_data.email])
		return save_data

	def __init__(self, *args, **kwargs):
		super(InscripcionForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control', 'required': True})
			if field == 'fullname':
				self.fields[field].widget.attrs.update({'class': 'form-control', 'pattern': '[A-Za-z]', 'required': True, 'title': 'Ingresa solo el nombre completo'})
			if field == 'telefono':
				self.fields[field].widget.attrs.update({'class': 'only-number form-control', 'required': True})