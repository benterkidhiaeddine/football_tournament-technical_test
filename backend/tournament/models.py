from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Equipe(TimeStampModel):
    nom = models.CharField(max_length=50, unique=True)
    ville = models.CharField(max_length=100)

    def __str__(self):
        # make sure it's unique using the id
        return f"{self.nom} ({self.id})"



class Joueur(TimeStampModel):
   
    class Post(models.TextChoices):
        ATTAQUANT = 'AT', _('Attaquant')
        MILIEU = 'MI', _('Milieu')
        DEFENSEUR = 'DE', _('Défenseur')
        GARDIEN = 'GA', _('Gardien')

    nom = models.CharField(max_length=50)
    poste = models.CharField(max_length=50, choices=Post.choices)

    def __str__(self):
        # make sure it's unique using the id
        return f"{self.nom} ({self.id})"
