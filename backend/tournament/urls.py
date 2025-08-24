from django.urls import path
from tournament import views

urlpatterns = [
    # Define your app routes here
    # equipe urls
    path("equipes/", views.equipe_list, name="equipe_list"),
    path("equipes/create/", views.equipe_create, name="equipe_create"),
    path("equipes/<int:pk>/edit/", views.equipe_edit, name="equipe_edit"),
    path("equipes/<int:pk>/delete/", views.equipe_delete, name="equipe_delete"),
    # joueur urls
    path("joueurs/", views.joueur_list, name="joueur_list"),
    path("joueurs/create/", views.joueur_create, name="joueur_create"),
    path("joueurs/<int:pk>/edit/", views.joueur_edit, name="joueur_edit"),
    path("joueurs/<int:pk>/delete/", views.joueur_delete, name="joueur_delete"),
    # match urls
    path("matchs/", views.match_list, name="match_list"),
    path("matchs/create/", views.match_create, name="match_create"),
    path("matchs/<int:pk>/edit/", views.match_edit, name="match_edit"),
    path("matchs/<int:pk>/delete/", views.match_delete, name="match_delete"),
    # classement
    path("classement/", views.classement, name="classement"),
]
