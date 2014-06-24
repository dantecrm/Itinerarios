from django.contrib import admin
from django.contrib.auth.models import User
from viajes.models import Persona, Coordinador, Secretaria, Anfitrion, Pastor, Incidentes, Comisiones, Itinerario_viaje


admin.site.register(Persona)
admin.site.register(Coordinador)
admin.site.register(Secretaria)
admin.site.register(Pastor)
admin.site.register(Anfitrion)
admin.site.register(Comisiones)
admin.site.register(Incidentes)
admin.site.register(Itinerario_viaje)
