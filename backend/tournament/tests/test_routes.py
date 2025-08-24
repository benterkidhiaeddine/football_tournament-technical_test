from django.test import TestCase
from django.urls import reverse
from tournament.models import Equipe, Joueur


class EquipeRoutesTest(TestCase):
    def setUp(self):
        self.equipe = Equipe.objects.create(nom="EquipeB", ville="VilleB")

    def test_equipe_list_route(self):
        url = reverse("equipe_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "equipe_list.html")

    def test_equipe_create_route(self):
        url = reverse("equipe_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "equipe_create_form.html")

    def test_equipe_edit_route(self):
        url = reverse("equipe_edit", args=[self.equipe.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("equipe", response.context)

    def test_equipe_delete_route(self):
        url = reverse("equipe_delete", args=[self.equipe.id])

        response = self.client.post(url, {"id": self.equipe.id})
        equipe = Equipe.objects.filter(id=self.equipe.id).first()
        self.assertIsNone(equipe)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("equipe_list"))


class JoueurRoutesTest(TestCase):
    def setUp(self):
        self.equipe = Equipe.objects.create(nom="EquipeC", ville="VilleC")
        self.joueur = Joueur.objects.create(nom="Binta", poste="MI", equipe=self.equipe)

    def test_joueur_list_route(self):
        url = reverse("joueur_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "joueur_list.html")

    def test_joueur_create_route(self):
        url = reverse("joueur_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "joueur_create_form.html")

    def test_joueur_edit_route(self):
        url = reverse("joueur_edit", args=[self.joueur.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("joueur", response.context)

    def test_joueur_delete_route(self):
        url = reverse("joueur_delete", args=[self.joueur.id])
        response = self.client.post(url, {"id": self.joueur.id})
        joueur = Joueur.objects.filter(id=self.joueur.id).first()
        self.assertIsNone(joueur)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("joueur_list"))
