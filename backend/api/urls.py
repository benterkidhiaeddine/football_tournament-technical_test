from django.urls import path
from api import views

urlpatterns = [
    # Define your app routes here
    # equipe urls
    path(
        "equipes/",
        views.EquipeViewSet.as_view({"get": "list", "post": "create"}),
        name="api_equipe_list",
    ),
    path(
        "equipes/<int:pk>/",
        views.EquipeViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="api_equipe_detail",
    ),
    # joueur urls
    path(
        "joueurs/",
        views.JoueurViewSet.as_view({"get": "list", "post": "create"}),
        name="api_joueur_list",
    ),

    path(
        "joueurs/<int:pk>/",
        views.JoueurViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="api_joueur_detail",
    ),
    # match urls
    path(
        "matchs/",
        views.MatchViewSet.as_view({"get": "list", "post": "create"}),
        name="api_match_list",
    ),
    path(
        "matchs/<int:pk>/",
        views.MatchViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="api_match_detail",
    ),
    # classement
    path("classement/", views.ClassementAPIView.as_view(), name="api_classement"),
]
