from django.contrib import admin
from tournament.models import Equipe, Joueur, Match

# Register your models here.


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ("nom", "ville", "created_at", "updated_at", "points")
    search_fields = ("nom", "ville")


@admin.register(Joueur)
class JoueurAdmin(admin.ModelAdmin):
    list_display = ("nom", "poste", "created_at", "updated_at")
    search_fields = ("nom", "poste")


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        "equipe_1",
        "equipe_2",
        "score_equipe_1",
        "score_equipe_2",
        "created_at",
        "updated_at",
    )
    search_fields = ("equipe_1__nom", "equipe_2__nom")
