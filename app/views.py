import requests
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Personaje, Arma
# Create your views here.


class FormList(ListView):
    model = Personaje
    template_name = "formulario_combate.html"
    context_object_name = "personajes"

    def get_queryset(self):
        return Personaje.objects.all()

class HomeView(TemplateView):
    template_name = "index.html"

class ListCharacters(ListView):
    model = Personaje
    template_name = "lista_personajes.html"
    context_object_name = "personajes"

    def get_queryset(self):
        return Personaje.objects.all()

class ListWeapons(ListView):
    model = Arma
    template_name = "lista_armas.html"
    context_object_name = "armas"

    def get_queryset(self):
        return Arma.objects.all()


class Combate:

    def combate(self):
        j1 = requests.get("j1")
        j2 = requests.get("j2")



