from tournament.models import Match
from api.serializers import MatchSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.shortcuts import render
from tournament.models import Equipe, Joueur
from rest_framework import viewsets

from api.serializers import EquipeSerializer, JoueurSerializer
from tournament.services import update_equipes_points

# Create your views here.


class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def perform_create(self, serializer):
        match = serializer.save()
        update_equipes_points(
            match.equipe_1,
            match.equipe_2,
            match.score_equipe_1,
            match.score_equipe_2,
        )

    def perform_update(self, serializer):
        match = serializer.save()
        update_equipes_points(
            match.equipe_1,
            match.equipe_2,
            match.score_equipe_1,
            match.score_equipe_2,
        )

    def perform_destroy(self, instance):
        update_equipes_points(
            instance.equipe_1,
            instance.equipe_2,
            instance.score_equipe_1,
            instance.score_equipe_2,
            match_deleted=True,
        )
        return super().perform_destroy(instance)


class ClassementAPIView(generics.ListAPIView):
    serializer_class = EquipeSerializer

    def get_queryset(self):
        return Equipe.objects.all().order_by("-points", "-buts_marques")
