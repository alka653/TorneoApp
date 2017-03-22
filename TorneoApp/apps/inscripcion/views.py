# -*- encoding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.shortcuts import render
from .forms import *

var_dir_template = 'inscripcion/'

class InscripcionView(SuccessMessageMixin, CreateView):
	template_name = var_dir_template+'index.html'
	success_message = 'Gracias por inscribirte, en tu email encontrarás información sobre el torneo.'
	form_class = InscripcionForm
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(InscripcionView, self).get_context_data(**kwargs)
		context['title'] = 'Torneo de ajedrez'
		return context