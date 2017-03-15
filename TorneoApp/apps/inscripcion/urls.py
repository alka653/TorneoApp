from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', InscripcionView.as_view(), name = 'inscripcion'),
]