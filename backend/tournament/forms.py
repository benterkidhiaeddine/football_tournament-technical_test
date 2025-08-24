from django import forms
from django.utils.translation import gettext_lazy as _
from tournament.models import Equipe, Joueur, Match


# Equipe Forms
class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ["id", "nom", "ville"]


# Joueur Forms
class JoueurForm(forms.ModelForm):

    class Meta:
        model = Joueur
        fields = ["id", "nom", "poste", "equipe"]

    # equipe can't have more than 11 players
    def clean_equipe(self):
        equipe = self.cleaned_data.get("equipe")
        if equipe and equipe.joueurs.count() >= 11:
            raise forms.ValidationError(_("Cette équipe a déjà 11 joueurs."))
        return equipe


# Match forms


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ["id", "equipe_1", "equipe_2", "score_equipe_1", "score_equipe_2"]
