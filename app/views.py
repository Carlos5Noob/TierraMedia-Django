import random

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

from django.shortcuts import render, redirect, get_object_or_404
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

        return redirect("combate", combate_creado.id, jugador1.id, jugador2.id)

    return render(request, "formulario_combate.html", {"personajes": personajes})


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



    if request.method == "POST":
        accion = request.POST.get("accion")

        if accion == "atacar":
            jugador1.mana += 10
            jugador1.save()
            jugador2.salud -= arma_jugador1.dano
            jugador2.save()
            mensaje = f"{jugador1.nombre} ataca a {jugador2.nombre}. ¡Le causa {arma_jugador1.dano} puntos de daño y recupera 10 de maná"

        elif "hb" in accion:
            opcion = accion
            mensaje = f"{jugador1.nombre} usa una habilidad especial."
            match opcion:
                case "hb1":
                    mensaje_accion = f"{jugador1.nombre} lanza una onda de energía a {jugador2.nombre} causandole 200 puntos de daño."
                    jugador2.salud -= 200
                case "hb2":
                    mensaje_accion = f"{jugador1.nombre} ataca con una púa venenosa a {jugador2.nombre} causandole 120 puntos de daño."
                    jugador2.salud -= 120
                    rng = random.randint(0,10)
                    if rng >= 7:
                        veneno = True
                        mensaje_veneno = f"{jugador2.nombre} ha sido envenenado"
                case "hb3":
                    mensaje_accion = f"{jugador1.nombre} se prepara para recibir el ataque"
                    guardia = True
                case "hb4":
                    mensaje_accion = f"{jugador1.nombre} canaliza su energía para realizar curar sus heridas"
                    jugador1.salud += 200
                    jugador1.save()

        if veneno:
            mensaje_veneno_2 = f"{jugador2.nombre} sufre daños de envenenamiento, pierde 100 puntos de vida"
            jugador2.salud -= 100

        mensaje_j2 = f"{jugador2.nombre} se prepara para atacar"

        if guardia:
            mensaje_guardia = f"{jugador1.nombre} ha encajado el golpe, no sufre daños"
        else:
            mensaje_dano = f"{jugador1.nombre} ha recibido el golpe, sufre {arma_jugador2.dano}"
            jugador1.salud -= arma_jugador2.dano

        return render(request, "resultado_combate.html", {
            "combate": combate_creado,
            "jugador1": jugador1,
            "jugador2": jugador2,
            "mensaje": mensaje,
            "mensaje_accion": mensaje_accion,
            "mensaje_veneno": mensaje_veneno,
            "mensaje_veneno_2": mensaje_veneno_2,
            "mensaje_guardia": mensaje_guardia,
            "mensaje_dano": mensaje_dano,
            "mensaje_j2": mensaje_j2
        })

    return render(request, "resultado_combate.html", {
        "combate": combate_creado,
        "jugador1": jugador1,
        "jugador2": jugador2,
    })