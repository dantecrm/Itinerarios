from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'viajes.views.Inicio', name="inicio"),
    url(r'^usuarios/$', 'viajes.views.Usuarios' , name="usuarios"),
    url(r'^itinerarios/$', 'viajes.views.itinerarios', name="itinerarios"),
    url(r'^comisiones/$', 'viajes.views.comisiones', name="comisiones"),
    url(r'^incidentes/$', 'viajes.views.incidentes', name="incidentes"),
    url(r'^media/(?P<path>.*)$', 'django.view.static.serve', {'document_root':settings.MEDIA_ROOT,}),
)
