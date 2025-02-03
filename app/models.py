from django.db import models

# Create your models here.

class Arma(models.Model):
    nombre = models.CharField(max_length=100)
    dano = models.IntegerField(default=0)
    critico = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    salud = models.IntegerField(default=200)
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

