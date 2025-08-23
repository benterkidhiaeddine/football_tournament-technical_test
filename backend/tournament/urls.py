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
]
