from django.shortcuts import render
from django.utils.translation.template import context_re
from django.views.generic import TemplateView, ListView

# Create your views here.


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



