from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=100)
    salud = models.IntegerField(default=200)



class Arma(models.Model):
    nombre = models.CharField(max_length=100)
    dano = models.IntegerField()
    critico = models.IntegerField()