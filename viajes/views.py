# coding: utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from viajes.models import Persona, Comisiones, Incidentes, Itinerario_viaje, Coordinador
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext

def Inicio(request):
    personas = Persona.objects.all()
    return render_to_response('viajes/inicio.html', {'personas':personas},
                              context_instance=RequestContext(request))

def Usuarios(request):
    usuarios = User.objects.all()
    titulo = "Página de usuarios registrados"
    return render_to_response('viajes/usuarios.html', {'usuarios':usuarios, 'titulo':titulo},
                              context_instance=RequestContext(request))

def itinerarios(request):
    itinerarios = Itinerario_viaje.objects.all()
    titulo = "Itinerarios hechos"
    return render_to_response('viajes/itinerarios.html',
                              {'itinerarios':itinerarios, 'titulo':titulo},
                              context_instance=RequestContext(request))

def comisiones(request):
    comisiones = Comisiones.objects.all()
    titulo = "Comisiones generales"
    return render_to_response('viajes/comisiones.html',
                              {'comisiones':comisiones, 'titulo':titulo},
                              context_instance=RequestContext(request))

def incidentes(request):
    incidentes = Incidentes.objects.all()
    titulo = "Problemas inesperados"
    return render_to_response('viajes/incidentes.html',
                              {'incidentes':incidentes, 'titulo':titulo},
                              context_instance=RequestContext(request))
