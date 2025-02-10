import random

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation.template import context_re
from django.views.generic import TemplateView, ListView, DetailView
from .models import Personaje, Arma, Faccion, Ubicacion, Combate


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

class DetailCharacters(DetailView):
    model = Personaje
    template_name = "app/detalles-personaje.html"
    context_object_name = "personaje"

class DetailArma(DetailView):
    model = Arma
    template_name = "app/detalles-arma.html"
    context_object_name = "arma"

class DetailFaccion(DetailView):
    model = Faccion
    template_name = "app/detalles-faccion.html"
    context_object_name = "faccion"

class DetailUbicacion(DetailView):
    model = Ubicacion
    template_name = "app/detalles-ubicacion.html"
    context_object_name = "ubicacion"

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
            return render(request, "app/formulario_combate.html", {"mensaje_error": mensaje_error, "personajes": personajes})

        if jugador1 == jugador2:
            mensaje_error = f"{jugador1} no puede luchar contra sí mismo."
            return render(request, "app/formulario_combate.html", {"mensaje_error": mensaje_error, "personajes": personajes})

        if Combate.objects.filter(nombre__iexact=nombre_combate).exists():
            mensaje_error = f"Esta batalla ( {nombre_combate} ) ya ha ocurrido en alguna parte de estas vastas tierras."
            return render(request, "app/formulario_combate.html", {"mensaje_error": mensaje_error, "personajes": personajes})

        combate_creado = Combate.objects.create(nombre=nombre_combate, luchador_1=jugador1, luchador_2=jugador2)

        return redirect("combate", combate_creado.id)

    return render(request, "app/formulario_combate.html", {"personajes": personajes})


def combate(request, combate_id):
    combate_creado = get_object_or_404(Combate, id=combate_id)
    jugador1 = combate_creado.luchador_1
    arma_jugador1 = Arma.objects.get(id=jugador1.arma_id)
    jugador2 = combate_creado.luchador_2
    arma_jugador2 = Arma.objects.get(id=jugador2.arma_id)
    veneno = None
    guardia = False

    mensaje = ""
    mensaje_accion = ""
    mensaje_veneno = ""
    mensaje_veneno_2 = ""
    mensaje_j2 = ""
    mensaje_guardia = ""
    mensaje_dano = ""
    mensaje_mana = ""
    derrota_j1 = ""
    derrota_j2 = ""

    if request.method == "POST":

        accion = request.POST.get("accion")
        if accion == "atacar":
            combate_creado.turnos += 1
            combate_creado.save()
            jugador1.mana += 10
            jugador1.save()
            jugador2.salud -= arma_jugador1.dano
            jugador2.save()
            mensaje = f"{jugador1.nombre} ataca a {jugador2.nombre}. ¡Le causa {arma_jugador1.dano} puntos de daño y recupera 10 de maná"

        elif "hb" in accion:
            combate_creado.turnos += 1
            combate_creado.save()
            opcion = accion
            mensaje = f"{jugador1.nombre} usa una habilidad especial."
            match opcion:
                case "hb1":
                    if jugador1.mana >= 50:
                        mensaje_accion = f"{jugador1.nombre} lanza una onda de energía a {jugador2.nombre} causandole 200 puntos de daño."
                        jugador2.salud -= 200
                        jugador1.mana -= 50
                        jugador1.save()
                        jugador2.save()
                    else:
                        mensaje_mana = f"{jugador1.nombre} no tiene suficiente mana para realizar su ataque, pierde su turno canalizando energía"
                        jugador1.mana += 5
                case "hb2":
                    if jugador1.mana >= 70:
                        mensaje_accion = f"{jugador1.nombre} ataca con una púa venenosa a {jugador2.nombre} causandole 120 puntos de daño."
                        jugador2.salud -= 120
                        jugador1.mana -= 70
                        jugador1.save()
                        jugador2.save()
                        rng = random.randint(0, 10)
                        if rng >= 7:
                            veneno = True
                            mensaje_veneno = f"{jugador2.nombre} ha sido envenenado"
                        else:
                            mensaje_mana = f"{jugador1.nombre} no tiene suficiente mana para realizar su ataque, pierde su turno canalizando energía"
                            jugador1.mana += 5
                case "hb3":
                    if jugador1.mana >= 30:
                        mensaje_accion = f"{jugador1.nombre} se prepara para recibir el ataque"
                        guardia = True
                        jugador1.mana -= 30
                        jugador1.save()
                    else:
                        mensaje_mana = f"{jugador1.nombre} no tiene suficiente mana para realizar su ataque, pierde su turno canalizando energía"
                        jugador1.mana += 5

                case "hb4":
                    if jugador1.mana >= 100:
                        jugador1.mana -= 100
                        mensaje_accion = f"{jugador1.nombre} canaliza su energía para realizar curar sus heridas"
                        jugador1.salud += 300
                        jugador1.save()
                    else:
                        mensaje_mana = f"{jugador1.nombre} no tiene suficiente mana para realizar su ataque, pierde su turno canalizando energía"
                        jugador1.mana += 5

        if veneno:
            mensaje_veneno_2 = f"{jugador2.nombre} sufre daños de envenenamiento, pierde 100 puntos de vida"
            jugador2.salud -= 100
            jugador2.save()

        if jugador2.salud <= 0:
            derrota_j2 = f"{jugador2.nombre} ha sido derrotado, enhorabuena"
            jugador2.salud = 200
            jugador2.save()
            return render(request, "app/resolucion.html", {"combate": combate_creado, "resolucion_2": derrota_j2})

        mensaje_j2 = f"{jugador2.nombre} se prepara para atacar"

        if guardia:
            mensaje_guardia = f"{jugador1.nombre} ha encajado el golpe, no sufre daños"
        else:
            mensaje_dano = f"{jugador1.nombre} ha recibido el golpe, sufre {arma_jugador2.dano} puntos de daño"
            jugador1.salud -= arma_jugador2.dano
            jugador1.save()

        return render(request, "app/resultado_combate.html", {
            "combate": combate_creado,
            "jugador1": jugador1,
            "jugador2": jugador2,
            "mensaje": mensaje,
            "mensaje_accion": mensaje_accion,
            "mensaje_veneno": mensaje_veneno,
            "mensaje_veneno_2": mensaje_veneno_2,
            "mensaje_guardia": mensaje_guardia,
            "mensaje_dano": mensaje_dano,
            "mensaje_j2": mensaje_j2,
            "mensaje_mana": mensaje_mana,
        })
    if jugador1.salud <= 0:
        derrota_j1 = f"{jugador1.nombre} ha sido derrotado, se acabó"
        return render(request, "app/resolucion.html", {"combate": combate_creado, "resolucion_1": derrota_j1})

    return render(request, "app/resultado_combate.html", {
        "combate": combate_creado,
        "jugador1": jugador1,
        "jugador2": jugador2,
    })