from django.urls import reverse
from django.test import TestCase

from app.models import Personaje, Arma, Faccion, Ubicacion


# Create your tests here.

class TemplatesTest(TestCase):
    """
    Tests for status code of templates
    """
    def setUp(self):
        self.response1 = self.client.get(reverse("index"))
        self.response2 = self.client.get(reverse("personajes"))
        self.response3 = self.client.get(reverse("armas"))
        self.response4 = self.client.get(reverse("ubicaciones"))
        self.response5 = self.client.get(reverse("facciones"))
        self.response6 = self.client.get(reverse("lucha"))

    # def test_templates(self):
    #     self.assertTemplateUsed(self.response1, "app/index.html")
    #     self.assertTemplateUsed(self.response2, "app/lista_personajes.html")
    #     self.assertTemplateUsed(self.response3, "app/lista_armas.html")
    #     self.assertTemplateUsed(self.response4, "app/lista_ubicaciones.html")
    #     self.assertTemplateUsed(self.response5, "app/lista_facciones.html")
    #     self.assertTemplateUsed(self.response6, "app/formulario_combate.html")

    def test_status(self):
        self.assertEqual(self.response1.status_code, 302)
        self.assertEqual(self.response2.status_code, 302)
        self.assertEqual(self.response3.status_code, 302)
        self.assertEqual(self.response4.status_code, 302)
        self.assertEqual(self.response5.status_code, 302)
        self.assertEqual(self.response6.status_code, 302)

class URLTest(TestCase):
    """
    Tests for urls
    """
    def setUp(self):
        pass
    def test_urls(self):
        self.assertURLEqual("/game/", reverse("index"))
        self.assertURLEqual("/game/personajes/", reverse("personajes"))
        self.assertURLEqual("/game/ubicaciones/", reverse("ubicaciones"))
        self.assertURLEqual("/game/facciones/", reverse("facciones"))
        self.assertURLEqual("/game/armas/", reverse("armas"))
        self.assertURLEqual("/game/combate/", reverse("lucha"))

class ModelsTest(TestCase):
    """
    Tests for models. Check if the models are created well. Also check if the str method works
    """
    def setUp(self):
        self.arma = Arma.objects.create(
            nombre = "Espadon",
            dano = 50,
            critico = 20
        )
        self.faccion = Faccion.objects.create(
            nombre = "Mordor",
            descripcion = "Descripcion"
        )
        self.ubicacion = Ubicacion.objects.create(
            nombre = "Madrid",
            descripcion = "Descripcion"
        )
        self.personaje = Personaje.objects.create(
            nombre = "Goku",
            salud = 100,
            mana = 100,
            arma = self.arma,
            faccion = self.faccion,
            ubicacion = self.ubicacion,
        )

    def test_personaje_str(self):
        self.assertEqual(str(self.personaje), "Goku")

    def test_arma_str(self):
        self.assertEqual(str(self.arma), "Espadon")

    def test_faccion_str(self):
        self.assertEqual(str(self.faccion), "Mordor")

    def test_ubicacion_str(self):
        self.assertEqual(str(self.ubicacion), "Madrid")