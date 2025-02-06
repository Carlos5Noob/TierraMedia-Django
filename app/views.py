from django.views.generic import TemplateView, ListView
from .models import Personaje, Arma


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

from django.shortcuts import render, redirect
from .models import Personaje, Combate

def pre_combate(request):
    """
    Aqui recogemos todos los requisitos que se necesitan antes de efectaur un combate y se comrpueban.
    Porque lo hacemos?: Para que todos los datos que se envíen sean correctos y no haya problemas a la hora de crear
    un combate, comprobamos que existan amobos jugadores, que no se hayan seleccionado dos jugadores iguales y que el
    nombre del combate sea único (Usamos iexact para que la comparación sea insensible a mayúsculas y minúsculas).
    """

    personajes = Personaje.objects.all()

    if request.method == "POST":
        nombre_combate = request.POST.get("nombre_combate")
        jugador1_id = request.POST.get('jugador1')
        jugador2_id = request.POST.get('jugador2')

        try:
            jugador1 = Personaje.objects.get(id=jugador1_id)
            jugador2 = Personaje.objects.get(id=jugador2_id)
        except Personaje.DoesNotExist:
            mensaje_error = "Debe seleccionar dos personajes válidos para el combate."
            return render(request, "formulario_combate.html", {"mensaje_error": mensaje_error, "personajes": personajes})

        if jugador1 == jugador2:
            mensaje_error = f"{jugador1} no puede luchar contra sí mismo."
            return render(request, "formulario_combate.html", {"mensaje_error": mensaje_error, "personajes": personajes})

        if Combate.objects.filter(nombre__iexact=nombre_combate).exists():
            mensaje_error = f"Esta batalla ( {nombre_combate} ) ya ha ocurrido en alguna parte de estas vastas tierras."
            return render(request, "formulario_combate.html", {"mensaje_error": mensaje_error, "personajes": personajes})

        combate_creado = Combate.objects.create(nombre=nombre_combate, luchador_1=jugador1, luchador_2=jugador2)

        return redirect("combate", combate_creado.id)

    return render(request, "formulario_combate.html", {"personajes": personajes})

def combate (request, combate_id):
    personajes = Personaje.objects.all()
    combate_creado = Combate.objects.get(id=combate_id)

    return render(request, "resultado_combate.html", {"combate": combate_creado, "personajes": personajes})


