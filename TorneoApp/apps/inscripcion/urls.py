from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', InscripcionView.as_view(), name = 'inscripcion'),
	url(r'^export/(?P<level>\w+)/$', export_data, name = 'export_data'),
]