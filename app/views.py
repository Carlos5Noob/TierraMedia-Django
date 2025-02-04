from django.shortcuts import render
from django.views import View
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


class Combate(View):

    def combate_view(self, request):
        personajes = Personaje.objects.all()

        if request.method == "POST":
            jugador1_id = request.POST.get('jugador1')
            jugador2_id = request.POST.get('jugador2')

            jugador1 = Personaje.objects.get(id=jugador1_id)
            jugador2 = Personaje.objects.get(id=jugador2_id)

            if not jugador1 or not jugador2:
                mensaje_error = "Debe introducir dos personajes para iniciar el combate"
                return render(request, "formulario_combate.html", {"mensaje_error": mensaje_error})

            if jugador1 is jugador2:
                mensaje_error = f"{jugador1} no puede luchar contra sí mismo"
                return render(request, "formulario_combate.html", {"mensaje_error": mensaje_error})

            return render(request, 'resultado_combate.html', {
                'jugador1': jugador1,
                'jugador2': jugador2,
            })

        return render(request, 'formulario_combate.html', {
            'personajes': personajes
        })

