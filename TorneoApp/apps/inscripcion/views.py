# -*- encoding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
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

def export_data(request, level):
	jugadores = Inscritos.objects.all().order_by('fullname')
	jugadores = jugadores if level == 'all' else jugadores.filter(nivel = level)
	content = 'No;NombreCompleto;Nombre;Apellido;\n'
	for jugador in jugadores:
		jugador_split = jugador.fullname.split(' ')
		content += str(jugador.pk)+';'+jugador.fullname.title()+';'+((jugador_split[0]+' '+jugador_split[1]).title() if len(jugador_split) == 4 else jugador_split[0].title())+';'+((jugador_split[2]+' '+jugador_split[3]).title() if len(jugador_split) == 4 else (jugador_split[1]+' '+jugador_split[2]).title())+';\n'
	response = HttpResponse(content, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=inscritos.TXT'
	return response