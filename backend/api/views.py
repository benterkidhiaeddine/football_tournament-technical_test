from django.shortcuts import render
from tournament.models import Equipe, Joueur
from rest_framework import viewsets

from api.serializers import EquipeSerializer, JoueurSerializer
# Create your views here.


class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer