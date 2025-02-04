from django.db import models

# Create your models here.

class Arma(models.Model):
    nombre = models.CharField(max_length=100)
    dano = models.IntegerField()
    critico = models.IntegerField()

    def __str__(self):
        return self.nombre

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    salud = models.IntegerField()
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Combate(models.Model):
    nombre = models.CharField(max_length=100)
    luchador_1 = models.ForeignKey(Personaje, on_delete=models.CASCADE, null=True, blank=True, related_name='luchador_1')
    luchador_2 = models.ForeignKey(Personaje, on_delete=models.CASCADE, null=True, blank=True, related_name='luchador_2')

    def __str__(self):
            return self.nombre