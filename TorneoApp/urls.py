from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^', include('TorneoApp.apps.inscripcion.urls')),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^admin/', admin.site.urls),
]
