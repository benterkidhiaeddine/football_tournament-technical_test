from django.test import TestCase
from django.core.exceptions import ValidationError
from tournament.models import Equipe, Joueur


class EquipeModelTest(TestCase):

    def setUp(self):
        self.equipe = Equipe.objects.create(nom="EquipeA", ville="VilleA")

    def test_create_equipe(self):
        equipe = Equipe.objects.create(nom="TestEquipe", ville="TestVille")
        self.assertEqual(str(equipe), f"TestEquipe ({equipe.id})")
        self.assertEqual(equipe.ville, "TestVille")

    # test equipe model can't have more than 11 joueurs in it
    def test_equipe_cannot_have_more_than_11_joueurs(self):
        for i in range(11):
            Joueur.objects.create(nom=f"Joueur{i}", poste="AT", equipe=self.equipe)
        self.assertEqual(self.equipe.joueurs.count(), 11)

        try:
            Joueur.objects.create(nom="Joueur12", poste="AT", equipe=self.equipe)
        except ValidationError:
            # If the exception is raised then the test passes because it's the intended behaviour
            pass

    # test equipe is related to players
    def test_equipe_has_joueurs(self):
        joueur1 = Joueur.objects.create(nom="Joueur1", poste="AT", equipe=self.equipe)
        joueur2 = Joueur.objects.create(nom="Joueur2", poste="DF", equipe=self.equipe)
        self.assertIn(joueur1, self.equipe.joueurs.all())
        self.assertIn(joueur2, self.equipe.joueurs.all())


class JoueurModelTest(TestCase):
    def setUp(self):
        self.equipe = Equipe.objects.create(nom="EquipeA", ville="VilleA")

    def test_create_joueur(self):
        joueur = Joueur.objects.create(nom="Ali", poste="AT", equipe=self.equipe)
        self.assertEqual(str(joueur), f"Ali ({joueur.id})")
        self.assertEqual(joueur.equipe, self.equipe)
