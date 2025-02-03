from django.db import models

# Create your models here.

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    salud = models.IntegerField(default=200)

    def __str__(self):
        return self.nombre

class Arma(models.Model):
    nombre = models.CharField(max_length=100)
    dano = models.IntegerField(default=0)
    critico = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre