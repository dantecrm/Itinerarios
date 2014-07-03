# coding: utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from django.db import models
from viajes.models import Persona, Comisiones, Incidentes, Itinerario_viaje, Coordinador
from viajes.forms import PersonaForm, ComisionesForm, IncidentesForm, Itinerario_viajeForm, DateForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils import timezone
from datetime import date, datetime

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
def borrar_itinerario(request, id):
    itinerario = get_object_or_404(Itinerario_viaje, pk=id)
    itinerario.delete()
    return HttpResponseRedirect("/itinerarios")

def editar_itinerario(request, id):
    itinerario = get_object_or_404(Itinerario_viaje, pk=id)
    if request.method == 'POST':
        formulario = Itinerario_viajeForm(request.POST, instance = itinerario)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/itinerarios")
    else:
        formulario = Itinerario_viajeForm(instance=itinerario)
    return render_to_response("viajes/itinerarioform.html",
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

def comisiones(request):
    comisiones = Comisiones.objects.all()
    titulo = "Comisiones generales"
    return render_to_response('viajes/comisiones.html',
                              {'comisiones':comisiones, 'titulo':titulo},
                              context_instance=RequestContext(request))

def borrar_comision(request, id):
    comision = get_object_or_404(Comisiones, pk=id)
    comision.delete()
    return HttpResponseRedirect("/comisiones")

def editar_comision(request, id):
    comision = get_object_or_404(Comisiones, pk=id)
    if request.method == 'POST':
        formulario = ComisionesForm(request.POST, instance = comision)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/comisiones")
    else:
        formulario = ComisionesForm(instance=comision)
    return render_to_response("viajes/comisionform.html",
                              {'formulario':formulario},
                              context_instance=RequestContext(request))


def incidentes(request):
    incidentes = Incidentes.objects.all()
    titulo = "Problemas inesperados"
    return render_to_response('viajes/incidentes.html',
                              {'incidentes':incidentes, 'titulo':titulo},
                              context_instance=RequestContext(request))

def borrar_incidente(request, id):
    incidente = get_object_or_404(Incidentes, pk=id)
    incidente.delete()
    return HttpResponseRedirect("/incidentes")

def editar_incidente(request, id):
    incidente = get_object_or_404(Incidentes, pk=id)
    if request.method == 'POST':
        formulario = IncidentesForm(request.POST, instance = incidente)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/incidentes")
    else:
        formulario = IncidentesForm(instance=incidente)
    return render_to_response("viajes/incidenteform.html",
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

def nuevo_itinerario(request):
    if request.method=='POST':
        formulario = Itinerario_viajeForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/itinerarios')
    else:
        formulario = Itinerario_viajeForm()
    return render_to_response('viajes/itinerarioform.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

def nueva_comision(request):
    if request.method=='POST':
        formulario = ComisionesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/comisiones')
    else:
        formulario = ComisionesForm()
    return render_to_response('viajes/comisionform.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/usuarios')
    else:
        formulario = UserCreationForm()
    return render_to_response('viajes/nuevousuario.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

def nuevo_incidente(request):
    if request.method=='POST':
        formulario = IncidentesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/incidentes')
    else:
        formulario = IncidentesForm()
    return render_to_response('viajes/incidenteform.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

def fecha(request):
    if request.method=='POST':
        formulario = DateForm(request.POST)
        mes = request.POST.get("mes")
    else:
        formulario = DateForm()
    return render_to_response('viajes/fecha.html',
                              {'formulario':formulario, 'mes':mes},
                              context_instance=RequestContext(request))

# def list_day(request):
#     dia = datetime(2014,6,30)
#     listas = Itinerario_viaje.objects.filter(fecha=dia)
#     return render_to_response('viajes/list_day.html', {'dia':dia, 'listas':listas},
#                               context_instance=RequestContext(request))

def list_day(request, dia):
    dia = datetime(aniox, mesx, diax)
    listas = Itinerario_viaje.objects.get(fecha__day=dia)
    return render_to_response('viajes/list_day.html', {'dia':dia, 'listas':listas},
                              context_instance=RequestContext(request))


def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('viajes/noactivo.html',
                                              context_instance=RequestContext(request))
            else:
                return render_to_response('viajes/nousuario.html',
                                          context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('viajes/ingresar.html', {'formulario': formulario},
                              context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('viajes/privado.html', {'usuario': usuario},
                              context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

