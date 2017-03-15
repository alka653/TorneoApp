from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('TorneoApp.apps.inscripcion.urls')),
	url(r'^admin/', admin.site.urls),
]
