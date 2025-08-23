from django.db import models
from django.core.exceptions import ValidationError
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

    def clean(self):
        if self.joueurs.count() >= 11:
            raise ValidationError(_("Une équipe ne peut pas avoir plus de 11 joueurs."))
        return super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        # make sure it's unique using the id
        return f"{self.nom} ({self.id})"


class Joueur(TimeStampModel):

    class Post(models.TextChoices):
        ATTAQUANT = "AT", _("Attaquant")
        MILIEU = "MI", _("Milieu")
        DEFENSEUR = "DE", _("Défenseur")
        GARDIEN = "GA", _("Gardien")

    nom = models.CharField(max_length=50)
    poste = models.CharField(max_length=50, choices=Post.choices)

    # when a team is deleted players will not be deleted they will just be free agents
    equipe = models.ForeignKey(
        Equipe, null=True, blank=True, on_delete=models.SET_NULL, related_name="joueurs"
    )

    #  Un joueur ne peut pas etre dans deux équipes au meme temps
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["nom", "equipe"], name="unique_player_in_team"
            ),
        ]

    def save(self, *args, **kwargs):
        self.equipe.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        # make sure it's unique using the id
        return f"{self.nom} ({self.id})"
