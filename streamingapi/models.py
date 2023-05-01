from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10)
    visualizaciones = models.IntegerField(default=0)
    puntaje = models.FloatField(default=0)
    suma_puntajes = models.FloatField(default=0)
    cantidad_puntuaciones = models.IntegerField(default=0)
class Serie(models.Model):
    nombre = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10)
    visualizaciones = models.IntegerField(default=0)
    puntaje = models.FloatField(default=0)
    suma_puntajes = models.FloatField(default=0)
    cantidad_puntuaciones = models.IntegerField(default=0)
