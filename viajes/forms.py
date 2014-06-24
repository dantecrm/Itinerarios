from django.forms import ModelForm
from django import forms
from viajes.models import Persona, Coordinador, Comisiones, Incidentes, Itinerario_viaje

# Formularios a partir de modelos

class PersonaForm(ModelForm):
    class Meta:
        model = Persona

class ComisionesForm(ModelForm):
    class Meta:
        model = Comisiones

class IncidentesForm(ModelForm):
    class Meta:
        model = Incidentes

class Itinerario_viajeForm(ModelForm):
    class Meta:
        model = Itinerario_viaje

