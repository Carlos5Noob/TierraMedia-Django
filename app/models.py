from django.db import models

# Create your models here.

class Arma(models.Model):
    nombre = models.CharField(max_length=100)
    dano = models.IntegerField()
    critico = models.IntegerField()

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Faccion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    salud = models.IntegerField()
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE)
    faccion = models.ForeignKey(Faccion, on_delete=models.CASCADE, null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

