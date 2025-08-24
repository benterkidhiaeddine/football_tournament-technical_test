from django.test import TestCase
from tournament.models import Equipe, Joueur
from tournament.forms import EquipeForm, JoueurForm


class EquipeFormTest(TestCase):
    def test_valid_equipe_form(self):
        form = EquipeForm(data={"nom": "EquipeForm", "ville": "VilleForm"})
        assert form.is_valid()

    def test_invalid_equipe_form(self):
        form = EquipeForm(data={"nom": "", "ville": ""})
        assert not form.is_valid()
        assert "nom" in form.errors
        assert "ville" in form.errors


class JoueurFormTest(TestCase):
    def setUp(self):
        self.equipe = Equipe.objects.create(
            nom="EquipeFormJoueur", ville="VilleFormJoueur"
        )

    def test_valid_joueur_form(self):
        form = JoueurForm(data={"nom": "Ali", "poste": "AT", "equipe": self.equipe.id})
        assert form.is_valid()

    def test_equipe_does_not_exist(self):
        form = JoueurForm(data={"nom": "Ali", "poste": "AT", "equipe": 999})
        assert not form.is_valid()
        assert "equipe" in form.errors

    def test_invalid_joueur_form_missing_fields(self):
        form = JoueurForm(data={"nom": "", "poste": "", "equipe": ""})
        assert not form.is_valid()
        assert "nom" in form.errors
        assert "poste" in form.errors

    def test_joueur_form_equipe_limit(self):
        # Add 11 joueurs to the equipe
        for i in range(11):
            Joueur.objects.create(nom=f"Player{i}", poste="AT", equipe=self.equipe)
        form = JoueurForm(
            data={"nom": "Extra", "poste": "AT", "equipe": self.equipe.id}
        )
        assert not form.is_valid()
        assert "equipe" in form.errors
