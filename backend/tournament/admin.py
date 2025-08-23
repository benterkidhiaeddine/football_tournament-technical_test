from django.contrib import admin
from tournament.models import Equipe, Joueur

# Register your models here.


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ("nom", "ville", "created_at", "updated_at")
    search_fields = ("nom", "ville")


@admin.register(Joueur)
class JoueurAdmin(admin.ModelAdmin):
    list_display = ("nom", "poste", "created_at", "updated_at")
    search_fields = ("nom", "poste")
