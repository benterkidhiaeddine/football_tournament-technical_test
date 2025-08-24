from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


# Create your models here
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Equipe(TimeStampModel):

    nom = models.CharField(max_length=50, unique=True)
    ville = models.CharField(max_length=100)
    points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    buts_marques = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    buts_recus = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def clean(self):
        if self.pk and self.joueurs.count() > 11:
            raise ValidationError(_("Une équipe ne peut pas avoir plus de 11 joueurs."))

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
        if self.equipe:
            # Check if adding this joueur would exceed the 11-player limit
            if self.pk:
                # Editing existing joueur: exclude self from count
                count = self.equipe.joueurs.exclude(pk=self.pk).count()
            else:
                count = self.equipe.joueurs.count()
            if count >= 11:
                raise ValidationError(_("Cette équipe a déjà 11 joueurs."))
        super().save(*args, **kwargs)

    def __str__(self):
        # make sure it's unique using the id
        return f"{self.nom} ({self.id})"


class Match(TimeStampModel):
    def clean(self):
        # Prevent a match with the same teams in any order
        if self.equipe_1 == self.equipe_2:

            raise ValidationError("Une équipe ne peut pas jouer contre elle-même.")
        # Check for existing match with same teams in any order
        existing = Match.objects.filter(
            models.Q(equipe_1=self.equipe_1, equipe_2=self.equipe_2)
            | models.Q(equipe_1=self.equipe_2, equipe_2=self.equipe_1)
        )
        if self.pk:
            existing = existing.exclude(pk=self.pk)
        if existing.exists():

            raise ValidationError("Un match entre ces deux équipes existe déjà.")

    equipe_1 = models.ForeignKey(
        Equipe, on_delete=models.CASCADE, related_name="matchs_equipe_1"
    )
    equipe_2 = models.ForeignKey(
        Equipe, on_delete=models.CASCADE, related_name="matchs_equipe_2"
    )
    score_equipe_1 = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    score_equipe_2 = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(score_equipe_1__gte=0) & models.Q(score_equipe_2__gte=0),
                name="scores can't be negative",
            ),
            # A team can't play against itself
            models.CheckConstraint(
                check=~models.Q(equipe_1=models.F("equipe_2")),
                name="different_teams",
            ),
        ]

    def __str__(self):
        return f"Match {self.id}: {self.equipe_1} vs {self.equipe_2}"
