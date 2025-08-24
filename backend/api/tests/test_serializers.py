from django.test import TestCase
from tournament.models import Equipe, Joueur
from api.serializers import EquipeSerializer, JoueurSerializer


class EquipeSerializerTest(TestCase):
    def test_equipe_serializer_valid(self):
        equipe = Equipe.objects.create(nom="EquipeTest", ville="VilleTest")
        serializer = EquipeSerializer(instance=equipe)
        data = serializer.data
        self.assertEqual(data["nom"], "EquipeTest")
        self.assertEqual(data["ville"], "VilleTest")

    def test_equipe_serializer_create(self):
        data = {"nom": "EquipeCreate", "ville": "VilleCreate"}
        serializer = EquipeSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        equipe = serializer.save()
        self.assertEqual(equipe.nom, "EquipeCreate")
        self.assertEqual(equipe.ville, "VilleCreate")


class JoueurSerializerTest(TestCase):
    def setUp(self):
        self.equipe = Equipe.objects.create(nom="EquipeJoueur", ville="VilleJoueur")

    def test_joueur_serializer_valid(self):
        joueur = Joueur.objects.create(nom="Ali", poste="AT", equipe=self.equipe)
        serializer = JoueurSerializer(instance=joueur)
        data = serializer.data
        self.assertEqual(data["nom"], "Ali")
        self.assertEqual(data["poste"], "AT")
        self.assertEqual(data["equipe"], self.equipe.id)

    def test_joueur_serializer_create(self):
        data = {"nom": "Binta", "poste": "MI", "equipe": self.equipe.id}
        serializer = JoueurSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        joueur = serializer.save()
        self.assertEqual(joueur.nom, "Binta")
        self.assertEqual(joueur.poste, "MI")
        self.assertEqual(joueur.equipe, self.equipe)

    def test_joueur_serializer_equipe_limit(self):
        # Add 11 joueurs to the equipe
        for i in range(11):
            Joueur.objects.create(nom=f"Player{i}", poste="AT", equipe=self.equipe)
        data = {"nom": "Extra", "poste": "AT", "equipe": self.equipe.id}
        serializer = JoueurSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("equipe", serializer.errors)
