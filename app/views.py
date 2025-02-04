from django.shortcuts import render
from django.utils.translation.template import context_re
from django.views.generic import TemplateView, ListView
from .models import Personaje, Arma, Faccion, Ubicacion


# Create your views here.


class HomeView(TemplateView):
    template_name = "app/index.html"

class ListCharacters(ListView):
    model = Personaje
    template_name = "app/lista_personajes.html"
    context_object_name = "personajes"

    def get_queryset(self):
        return Personaje.objects.all()

class ListWeapons(ListView):
    model = Arma
    template_name = "app/lista_armas.html"
    context_object_name = "armas"

    def get_queryset(self):
        return Arma.objects.all()

class ListFactions(ListView):
    model = Faccion
    template_name = "app/lista_facciones.html"
    context_object_name = "facciones"

    def get_queryset(self):
        return Faccion.objects.all()

class Ubicaciones(ListView):
    model = Ubicacion
    template_name = "app/lista_ubicaciones.html"
    context_object_name = "ubicaciones"

    def get_queryset(self):
        return Ubicacion.objects.all()