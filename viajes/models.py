# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Persona(User):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    Email = models.CharField(max_length=50, unique=True)
    documento_identificacion = models.CharField(max_length=10, unique=True)
    foto = models.ImageField(upload_to='imagenes', verbose_name='Fotografia', null=True)

    def __unicode__(self):
        return "%s %s" %(self.nombre, self.documento_identificacion)

class Coordinador(models.Model):
    coordinador = models.ForeignKey(Persona)

    def __unicode__(self):
        return "%s %s" %(self.coordinador.nombre,
                         self.coordinador.documento_identificacion)

class Secretaria(models.Model):
    secretaria = models.ForeignKey(Persona)

    def __unicode__(self):
        return "%s %s" %(self.secretaria.nombre,
                         self.secretaria.documento_identificacion)

class Pastor(models.Model):
    pastor = models.ForeignKey(Persona)

    def __unicode__(self):
        return "%s %s" %(self.pastor.nombre,
                         self.pastor.documento_identificacion)

class Anfitrion(models.Model):
    anfitrion = models.ForeignKey(Persona)

    def __unicode__(self):
        return "%s %s" %(self.anfitrion.nombre,
                         self.anfitrion.documento_identificacion)

class Comisiones(models.Model):
    pastor_viajero = models.ForeignKey(Pastor)
    motivo = models.TextField(verbose_name="Motivo del Viaje")
    anfitrion_recogedor = models.ForeignKey(Anfitrion)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return "%s: Pastor => %s" %(self.motivo, self.pastor_viajero.pastor.nombre)

class Incidentes(models.Model):
    comision = models.ForeignKey(Comisiones)
    suceso = models.TextField(verbose_name="Suceso de Retraso")
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.comision.motivo

TIPO_TRANSPORTE = (
    ('A', 'Aereo'),
    ('T', 'Terrestre'),
    ('M', 'Maritimo'),
)

UNION = (
    ('S', 'Unión del Sur'),
    ('N', 'Unión del Norte'),
)

class Itinerario_viaje(models.Model):
    cod_reserva = models.CharField(max_length=6, unique=True,
                                   help_text="Por favor escriba con mayúsculas")
    hora_partida = models.TimeField(verbose_name="Hora de partida")
    hora_llegada = models.TimeField(verbose_name="Hora de llegada")
    origen = models.CharField(max_length=50, verbose_name="Ciudad de Origen")
    destino = models.CharField(max_length=50, verbose_name="Ciudad de llegada")
    ruc = models.IntegerField(unique=True)
    tipo_transporte = models.CharField(max_length=1,
                                       choices=TIPO_TRANSPORTE, default='A')
    fecha = models.DateField()
    mision = models.CharField(max_length=1, choices=UNION, default='N')
    comision = models.ForeignKey(Comisiones)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return "De %s a %s" %(self.origen, self.destino)
