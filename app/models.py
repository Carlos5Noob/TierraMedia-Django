from django.db import models

# Create your models here.

class Arma(models.Model):
    """
    Modelo para las armas
    """
    nombre = models.CharField(max_length=100)
    dano = models.IntegerField()
    critico = models.IntegerField()

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    """
    Modelo para las ubicaciones
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Faccion(models.Model):
    """
    Modelo para las facciones
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Personaje(models.Model):
    """
    Modelo para los personajes
    Cada personaje tiene una clave foránea con las armas, facciones y ubicaciones
    """
    nombre = models.CharField(max_length=120)
    salud = models.IntegerField()
    mana = models.IntegerField(default=400)
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE)
    faccion = models.ForeignKey(Faccion, on_delete=models.CASCADE, null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos_proyecto/',null=True, blank=True)

    def __str__(self):
        return self.nombre

class Combate(models.Model):
    """
    Modelo para los combates
    """
    nombre = models.CharField(max_length=100)
    luchador_1 = models.ForeignKey(Personaje, on_delete=models.CASCADE, null=True, blank=True, related_name='luchador_1')
    luchador_2 = models.ForeignKey(Personaje, on_delete=models.CASCADE, null=True, blank=True, related_name='luchador_2')
    turnos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre}: {self.luchador_1} vs {self.luchador_2}"