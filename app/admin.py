from django.contrib import admin

from .models import Personaje, Arma, Faccion

# Register your models here.

admin.site.register(Personaje)
admin.site.register(Arma)
admin.site.register(Faccion)
