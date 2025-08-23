from tournament.models import Equipe, Joueur
from django import forms

# Equipe Forms
class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ["id", "nom", "ville"]


# Joueur Forms
class JoueurForm(forms.ModelForm):
    
    class Meta:
        model = Joueur
        fields = ["id", "nom", "poste"]
