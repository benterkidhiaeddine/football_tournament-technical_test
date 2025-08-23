from tournament.models import Equipe, Joueur

from rest_framework import serializers


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
