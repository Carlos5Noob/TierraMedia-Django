from django.db import models

# Create your models here.

class Arma(models.Model):
    nombre = models.CharField(max_length=50)
    potencia = models.IntegerField()

    def __str__(self):
        return self.nombre

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    arma = models.ManyToManyField(Arma)

    def __str__(self):
        return self.nombre