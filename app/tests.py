from django.urls import reverse
from django.test import TestCase

# Create your tests here.

class TemplatesTest(TestCase):
    def setUp(self):
        self.response1 = self.client.get(reverse("index"))
        self.response2 = self.client.get(reverse("personajes"))
        self.response3 = self.client.get(reverse("armas"))
        self.response4 = self.client.get(reverse("ubicaciones"))
        self.response5 = self.client.get(reverse("facciones"))
        self.response6 = self.client.get(reverse("lucha"))

    def test_templates(self):
        self.assertTemplateUsed(self.response1, "app/index.html")
        self.assertTemplateUsed(self.response2, "app/lista_personajes.html")
        self.assertTemplateUsed(self.response3, "app/lista_armas.html")
        self.assertTemplateUsed(self.response4, "app/lista_ubicaciones.html")
        self.assertTemplateUsed(self.response5, "app/lista_facciones.html")
        self.assertTemplateUsed(self.response6, "app/formulario_combate.html")

    def test_status(self):
        self.assertEqual(self.response1.status_code, 302)
        self.assertEqual(self.response2.status_code, 302)
        self.assertEqual(self.response3.status_code, 302)
        self.assertEqual(self.response4.status_code, 302)
        self.assertEqual(self.response5.status_code, 302)
        self.assertEqual(self.response6.status_code, 302)

class URLTest(TestCase):
    def setUp(self):
        pass
    def test_urls(self):
        self.assertURLEqual("/game/", reverse("index"))
        self.assertURLEqual("/game/personajes/", reverse("personajes"))
        self.assertURLEqual("/game/ubicaciones/", reverse("ubicaciones"))
        self.assertURLEqual("/game/facciones/", reverse("facciones"))
        self.assertURLEqual("/game/armas/", reverse("armas"))
        self.assertURLEqual("/game/combate/", reverse("lucha"))
