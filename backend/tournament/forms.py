from tournament.models import Equipe, Joueur
# Create the form for create a team
class CreateEquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nom', 'ville']

        

# Create the form for create a player
class CreateJoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['nom', 'poste']


