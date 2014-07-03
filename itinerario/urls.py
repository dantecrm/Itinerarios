from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^$', 'viajes.views.Inicio', name="inicio"),
    url(r'^usuarios/$', 'viajes.views.Usuarios' , name="usuarios"),
    url(r'^itinerarios/$', 'viajes.views.itinerarios', name="itinerarios"),
    url(r'^comisiones/$', 'viajes.views.comisiones', name="comisiones"),
    url(r'^incidentes/$', 'viajes.views.incidentes', name="incidentes"),
    url(r'^itinerario/nuevo/$', 'viajes.views.nuevo_itinerario', name="nuevo_itinerario"),
    url(r'^comision/nueva/$', 'viajes.views.nueva_comision', name="nueva_comision"),
    url(r'^usuario/nuevo/$', 'viajes.views.nuevo_usuario', name="nuevo_usuario"),
    url(r'^incidente/nuevo/$', 'viajes.views.nuevo_incidente', name="nuevo_incidente"),
    url(r'^fecha/$', 'viajes.views.fecha', name="fecha"),
    url(r'^borrar/itinerario/(?P<id>\d+)$', 'viajes.views.borrar_itinerario'),
    url(r'^editar/itinerario/(?P<id>\d+)$', 'viajes.views.editar_itinerario'),
    url(r'^borrar/comision/(?P<id>\d+)$', 'viajes.views.borrar_comision'),
    url(r'^editar/comision/(?P<id>\d+)$', 'viajes.views.editar_comision'),
    url(r'^editar/incidente/(?P<id>\d+)$', 'viajes.views.editar_incidente'),
    url(r'^borrar/incidente/(?P<id>\d+)$', 'viajes.views.borrar_incidente'),
    url(r'^ingresar/$', 'viajes.views.ingresar', name='ingresar'),
    url(r'^privado/$', 'viajes.views.privado', name='privado'),
    url(r'^cerrar/$', 'viajes.views.cerrar', name='cerrar'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^itinerario/list_day/$', 'viajes.views.list_day', name="list_day"),
#    url(r'^itinerario/list_month/$', 'viajes.views.list_month', name="list_month"),
#    url(r'^itinerario/list_year/$', 'viajes.views.list_year', name="list_year"),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
