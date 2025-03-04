import random
import urllib.parse
from django.urls import reverse
from random import randint

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request

from django.views.generic import TemplateView, ListView, DetailView
from .models import Personaje, Arma, Faccion, Ubicacion, Combate


# Crea tus vistas aquí.

# Todas las vistas están basadas en clases (excepto las de combate), para mejorar la reusabilidad del código y la escalabilidad del proyecto.
class InicioView(TemplateView):
    template_name = "app/inicio.html"

class HomeView(LoginRequiredMixin, TemplateView):
    """
    Vista para la página principal. (index)
    """
    template_name = "app/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context

class ListCharacters(LoginRequiredMixin, ListView):
    """
    Vista para la lista de personajes.
    Hay un botón para filtrarlos por facciones.
    """
    model = Personaje
    template_name = "app/lista_personajes.html"
    context_object_name = "personajes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["facciones"] = Faccion.objects.all()
        return context

    def get_queryset(self):
        faccion_id = self.request.GET.get("faccion")
        if faccion_id and faccion_id.isdigit():
            return Personaje.objects.filter(faccion_id=faccion_id)
        return Personaje.objects.all()


class ListWeapons(LoginRequiredMixin, ListView):
    """
    Vista para la lista de armas.
    """
    model = Arma
    template_name = "app/lista_armas.html"
    context_object_name = "armas"

    def get_queryset(self):
        return Arma.objects.all()

class ListFactions(LoginRequiredMixin, ListView):
    """
    Vista para la lista de facciones.
    """
    model = Faccion
    template_name = "app/lista_facciones.html"
    context_object_name = "facciones"

    def get_queryset(self):
        return Faccion.objects.all()

class Ubicaciones(LoginRequiredMixin, ListView):
    """
    Vista para la lista de ubicaciones.
    """
    model = Ubicacion
    template_name = "app/lista_ubicaciones.html"
    context_object_name = "ubicaciones"

    def get_queryset(self):
        return Ubicacion.objects.all()

class DetailCharacters(LoginRequiredMixin, DetailView):
    """
    Vista para los detalles de los personajes.
    Esta clase recoge el ID del personaje y lo envía a la plantilla.
    """
    model = Personaje
    template_name = "app/detalles-personaje.html"
    context_object_name = "personaje"

class DetailArma(LoginRequiredMixin, DetailView):
    """
    Vista para los detalles de las armas.
    Esta clase recoge el ID del arma y lo envía a la plantilla.
    """
    model = Arma
    template_name = "app/detalles-arma.html"
    context_object_name = "arma"

class DetailFaccion(LoginRequiredMixin, DetailView):
    """
    Vista para los detalles de la facción.
    Esta clase recoge el ID de la facción y lo envía a la plantilla.
    """
    model = Faccion
    template_name = "app/detalles-faccion.html"
    context_object_name = "faccion"

class DetailUbicacion(LoginRequiredMixin, DetailView):
    """
    Vista para los detalles de la ubicación.
    Esta clase recoge el ID de la ubicación y lo envía a la plantilla.
    """
    model = Ubicacion
    template_name = "app/detalles-ubicacion.html"
    context_object_name = "ubicacion"

# Vistas para el combate basadas en funciones.
@login_required()
def pre_combate(request):
    """
    Aquí recogemos todos los requisitos que se necesitan antes de efectuar un combate y se comprueban.
    Porque lo hacemos?: Para que todos los datos que se envíen sean correctos y no haya problemas a la hora de crear
    un combate, comprobamos que existan ambos jugadores, que no se hayan seleccionado dos jugadores iguales y que el
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

@login_required
def combate(request, combate_id):
    """
    Aquí recogemos todos los requisitos que se necesitan para efectuar un combate
    """
    combate_creado = get_object_or_404(Combate, id=combate_id)
    jugador1 = combate_creado.luchador_1
    arma_jugador1 = Arma.objects.get(id=jugador1.arma_id)
    jugador2 = combate_creado.luchador_2
    arma_jugador2 = Arma.objects.get(id=jugador2.arma_id)
    veneno = None
    veneno_j2 = None
    guardia = False

    mensaje = ""
    mensaje_accion = ""
    mensaje_veneno = ""
    mensaje_veneno_2 = ""
    mensaje_veneno_j2 = ""
    mensaje_veneno_j2_2 = ""
    mensaje_j2 = ""
    mensaje_accion_j2 = ""
    mensaje_guardia = ""
    mensaje_dano = ""
    mensaje_mana = ""
    mensaje_adicional = ""
    mensaje_adicional_2 = ""
    derrota_j1 = ""
    derrota_j2 = ""

    if request.method == "POST":

        accion = request.POST.get("accion")
        if accion == "atacar":
            combate_creado.turnos += 1
            combate_creado.save()
            jugador1.mana += 10
            jugador1.save()
            if chances():
                critico = arma_jugador1.dano + arma_jugador1.critico
                jugador2.salud -= critico
                mensaje = f"{jugador1.nombre} acierta un golpe certero a {jugador2.nombre}. ¡Le causa {critico} puntos de daño y recupera 10 de maná!"
            else:
                jugador2.salud -= arma_jugador1.dano
                mensaje = f"{jugador1.nombre} ataca a {jugador2.nombre}. ¡Le causa {arma_jugador1.dano} puntos de daño y recupera 10 de maná!"
            if chances():
                mensaje_adicional = f"{jugador1.nombre} ha pillado desprevenido a {jugador2.nombre}, ha logrado atacar otra vez!"
                if chances():
                    critico = arma_jugador1.dano + arma_jugador1.critico
                    jugador2.salud -= critico
                    mensaje_adicional_2 = f"{jugador1.nombre} acierta un golpe certero a {jugador2.nombre}. ¡Le causa {critico} puntos de daño y recupera 10 de maná!"
                else:
                    jugador2.salud -= arma_jugador1.dano
                    mensaje_adicional_2 = f"{jugador1.nombre} ataca a {jugador2.nombre}. ¡Le causa {arma_jugador1.dano} puntos de daño y recupera 10 de maná!"
            jugador2.save()


        elif "hb" in accion:
            combate_creado.turnos += 1
            combate_creado.save()
            opcion = accion
            mensaje = f"{jugador1.nombre} usa una habilidad especial."
            match opcion:
                case "hb1":
                    if jugador1.mana >= 50:
                        mensaje_accion = f"{jugador1.nombre} lanza una onda de energía a {jugador2.nombre} causandole 150 puntos de daño."
                        jugador2.salud -= 150
                        jugador1.mana -= 50
                        jugador1.save()
                        jugador2.save()
                    else:
                        mensaje_mana = f"{jugador1.nombre} no tiene suficiente mana para realizar su ataque, pierde su turno canalizando energía."
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
                            mensaje_veneno = f"{jugador2.nombre} ha sido envenenado."
                    else:
                        mensaje_mana = f"{jugador1.nombre} no tiene suficiente mana para realizar su ataque, pierde su turno canalizando energía."
                        jugador1.mana += 5
                case "hb3":
                    if jugador1.mana >= 30:
                        mensaje_accion = f"{jugador1.nombre} se prepara para recibir el ataque."
                        guardia = True
                        jugador1.mana -= 30
                        jugador1.save()
                    else:
                        mensaje_mana = f"{jugador1.nombre} no tiene suficiente mana para realizar su ataque, pierde su turno canalizando energía."
                        jugador1.mana += 5

                case "hb4":
                    if jugador1.mana >= 100:
                        jugador1.mana -= 100
                        mensaje_accion = f"{jugador1.nombre} canaliza su energía para realizar curar sus heridas."
                        jugador1.salud += 300
                        jugador1.save()
                    else:
                        mensaje_mana = f"{jugador1.nombre} no tiene suficiente mana para realizar su ataque, pierde su turno canalizando energía."
                        jugador1.mana += 5

        if veneno:
            mensaje_veneno_2 = f"{jugador2.nombre} sufre daños de envenenamiento, pierde 100 puntos de vida."
            jugador2.salud -= 100
            jugador2.save()

        if jugador2.salud <= 0:
            derrota_j2 = f"{jugador2.nombre} ha sido derrotado, enhorabuena"
            jugador1.victorias += 1
            jugador1.save()
            jugador2.derrotas += 1
            jugador2.salud = 200
            jugador2.save()
            return render(request, "app/resolucion.html", {"combate": combate_creado, "resolucion_2": derrota_j2})

        if not chances():
            mensaje_j2 = f"{jugador2.nombre} se prepara para atacar."
            if guardia:
                mensaje_guardia = f"{jugador1.nombre} ha encajado el golpe, no sufre daños."
            else:
                mensaje_dano = f"{jugador1.nombre} ha recibido el golpe, sufre {arma_jugador2.dano} puntos de daño."
                jugador1.salud -= arma_jugador2.dano
                jugador1.save()
        else:
            mensaje_j2 = f"{jugador2.nombre} se prepara para lanzar un ataque especial."

            ataque_especial = randint(1,3)

            match ataque_especial:
                case 1:
                    mensaje_accion_j2 = f"{jugador2.nombre} ha lanza una onda de energía a {jugador1.nombre} causandole 200 puntos de daño."
                    jugador1.salud -= 200
                    jugador1.save()
                case 2:
                    mensaje_accion_j2 = f"{jugador2.nombre} ataca con una púa venenosa a {jugador1.nombre} causandole 120 puntos de daño."
                    jugador1.salud -= 120
                    rng = random.randint(0, 10)
                    if rng >= 7:
                        veneno_j2 = True
                        mensaje_veneno_j2 = f"{jugador1.nombre} ha sido envenenado."
                case 3:
                    mensaje_accion_j2 = f"{jugador2.nombre} canaliza su energía para realizar curar sus heridas, recupera 300 puntos de vida."
                    jugador2.salud += 300
                    jugador2.save()

            if veneno_j2:
                mensaje_veneno_j2_2 = f"{jugador2.nombre} sufre daños de envenenamiento, pierde 100 puntos de vida."
                jugador2.salud -= 100
                jugador2.save()

        if jugador1.salud <= 0:
            derrota_j1 = f"{jugador1.nombre} ha sido derrotado, se acabó"
            jugador2.victorias += 1
            jugador2.save()
            jugador1.salud = 1
            jugador1.derrotas += 1
            jugador1.save()
            return render(request, "app/resolucion.html", {"combate": combate_creado, "resolucion_1": derrota_j1})

        return render(request, "app/resultado_combate.html", {
            "combate": combate_creado,
            "jugador1": jugador1,
            "jugador2": jugador2,
            "mensaje": mensaje,
            "mensaje_accion": mensaje_accion,
            "mensaje_adicional": mensaje_adicional,
            "mensaje_adicional_2": mensaje_adicional_2,
            "mensaje_veneno": mensaje_veneno,
            "mensaje_veneno_2": mensaje_veneno_2,
            "mensaje_guardia": mensaje_guardia,
            "mensaje_dano": mensaje_dano,
            "mensaje_j2": mensaje_j2,
            "mensaje_accion_j2": mensaje_accion_j2,
            "mensaje_veneno_j2" : mensaje_veneno_j2,
            "mensaje_veneno_j2_2" : mensaje_veneno_j2_2,
            "mensaje_mana": mensaje_mana,
        })

    return render(request, "app/resultado_combate.html", {
        "combate": combate_creado,
        "jugador1": jugador1,
        "jugador2": jugador2,
    })

def chances():
    """
    Función para calcular las probabilidades de que el segundo jugador pueda realizar un ataque especial.
    """
    rng = randint(1, 10)
    if rng == 1:
        return True
    else:
        return False

# Función para controlar la taberna
@login_required()
def taberna(request):
    """
    Vista para la taberna, aquí el jugador puede descansar para recuperar su salud, hablar con el tabernero, jugar a los dados con él, etc.
    """
    mensaje = request.GET.get('mensaje')
    if request.method == "POST":
        personajes = Personaje.objects.all()
        for personaje in personajes:
            personaje.salud = 300
            personaje.save()
        return render(request, "app/taberna.html", context={"descanso": "Todos los personajes se han restaurado correctamente"})
    return render(request, "app/taberna.html", context={"mensaje": mensaje})

def hablar_npc(request):
    frases = [
        "Escuché que hay un tesoro escondido en el bosque...",
        "Dicen que un dragón fue visto cerca de la montaña.",
        "Ten cuidado con los bandidos del camino del sur.",
        "Las mejores armas se venden en la ciudad capital.",
        "Escuché que en el bosque al norte hay un guerrero maldito… nadie que lo ha visto ha vuelto para contarlo.",
        "Dicen que un dragón fue visto cerca de la montaña. ¿Será verdad o solo habladurías?",
        "Las ruinas antiguas de los elfos esconden un poder que muchos desean… pero pocos sobreviven para obtenerlo.",
        "Hay un pasadizo secreto en las alcantarillas de la ciudad. Solo los ladrones lo conocen.",
        "Un viajero me dijo que en el pueblo vecino hay alguien que paga bien por hierbas raras.",
        "Ten cuidado con los bandidos del camino del sur, no respetan ni a los mercaderes ni a los aventureros.",
        "Hace años, un mago loco selló un demonio en la cueva al este. Pero las puertas han empezado a crujir…"
    ]
    mensaje = random.choice(frases)

    # esto lo hago para codificar el mensaje
    mensaje_codificado = urllib.parse.quote(mensaje)

    return redirect(reverse('taberna') + f'?mensaje={mensaje_codificado}')

def dados(request):

    """
    Vista para el juego de los dados.
    """

    resultado = None
    dado_jugador = None
    dado_tabernero = None

    if request.method == "POST":
        dado_jugador = random.randint(1, 6)
        dado_tabernero = random.randint(1, 6)

        if dado_jugador > dado_tabernero:
            resultado = "¡Ganaste! 🍻"
        elif dado_jugador < dado_tabernero:
            resultado = "El tabernero gana. ¡Suerte la próxima vez! 😆"
        else:
            resultado = "Empate. ¡Lanza otra vez! 🎲"

    return render(request, "app/dados.html", {
        "dado_jugador": dado_jugador,
        "dado_tabernero": dado_tabernero,
        "resultado": resultado
    })

def crear_personaje(request):

    """
    Vista para la creación de personajes.
    """

    armas = Arma.objects.all()
    facciones = Faccion.objects.all()
    ubicaciones = Ubicacion.objects.all()

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        salud = request.POST.get("salud")
        mana = request.POST.get("mana")
        arma = request.POST.get("arma")
        faccion = request.POST.get("faccion")
        ubicacion = request.POST.get("ubicacion")
        foto = request.FILES.get("foto")
        personaje = Personaje.objects.create(
            nombre = nombre,
            salud = salud,
            mana = mana,
            arma_id = arma,
            faccion_id = faccion,
            ubicacion_id = ubicacion, 
            foto = foto
        )

        personaje.save()

        return render(request, "app/crear_personaje.html", {"mensaje": "Personaje creado correctamente"})

    return render(request, "app/crear_personaje.html", {
        "armas": armas,
        "facciones": facciones,
        "ubicaciones": ubicaciones
    })

class RegistroCombates(LoginRequiredMixin, ListView):   
    """
    Vista para el registro de combates.
    """
    model = Combate
    template_name = "app/registro-combates.html"
    context_object_name = "combates"

    def get_queryset(self):
        return Combate.objects.filter(nombre__isnull=False).exclude(nombre="").filter(turnos__gt=0) 
        # excluimos los combates sin nombre y los combates sin turnos
    