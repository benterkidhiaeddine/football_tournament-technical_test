from django.db import models
from rest_framework import serializers
from tournament.models import Equipe, Joueur, Match
from tournament.services import update_equipes_points


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = "__all__"


class JoueurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joueur
        fields = "__all__"

    def validate_equipe(self, value):
        if value.joueurs.count() >= 11:
            raise serializers.ValidationError("Cette équipe a déjà 11 joueurs.")
        return value


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"

    def validate(self, data):
        equipe_1 = data.get("equipe_1")
        equipe_2 = data.get("equipe_2")
        if equipe_1 == equipe_2:
            raise serializers.ValidationError(
                "Une équipe ne peut pas jouer contre elle-même."
            )
        # Check for existing match with same teams in any order
        existing = Match.objects.filter(
            (
                models.Q(equipe_1=equipe_1, equipe_2=equipe_2)
                | models.Q(equipe_1=equipe_2, equipe_2=equipe_1)
            )
        )
        if self.instance:
            existing = existing.exclude(pk=self.instance.pk)
        if existing.exists():
            raise serializers.ValidationError(
                "Un match entre ces deux équipes existe déjà."
            )
        return data
