from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tournament.models import Equipe, Joueur


class EquipeAPIRoutesTest(APITestCase):
    def setUp(self):
        self.equipe = Equipe.objects.create(nom="EquipeAPI", ville="VilleAPI")

    def test_list_equipes(self):
        url = reverse("api_equipe_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_equipe(self):
        url = reverse("api_equipe_list")
        data = {"nom": "EquipeNew", "ville": "VilleNew"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_equipe(self):
        url = reverse("api_equipe_detail", args=[self.equipe.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_equipe(self):
        url = reverse("api_equipe_detail", args=[self.equipe.id])
        data = {"nom": "EquipeUpdated", "ville": "VilleUpdated"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_equipe(self):
        url = reverse("api_equipe_detail", args=[self.equipe.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class JoueurAPIRoutesTest(APITestCase):
    def setUp(self):
        self.equipe = Equipe.objects.create(
            nom="EquipeJoueurAPI", ville="VilleJoueurAPI"
        )
        self.joueur = Joueur.objects.create(nom="Ali", poste="AT", equipe=self.equipe)

    def test_list_joueurs(self):
        url = reverse("api_joueur_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_joueur(self):
        url = reverse("api_joueur_list")
        data = {"nom": "Binta", "poste": "MI", "equipe": self.equipe.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_joueur(self):
        url = reverse("api_joueur_detail", args=[self.joueur.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_joueur(self):
        url = reverse("api_joueur_detail", args=[self.joueur.id])
        data = {"nom": "AliUpdated", "poste": "DE", "equipe": self.equipe.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_joueur(self):
        url = reverse("api_joueur_detail", args=[self.joueur.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
