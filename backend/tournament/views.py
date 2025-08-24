from django.shortcuts import render, redirect, get_object_or_404
from tournament.models import Equipe, Joueur, Match
from tournament.forms import EquipeForm, JoueurForm, MatchForm
from tournament.services import update_equipes_points


# Create your views here.


# home view
def home(request):
    return render(request, "home.html")


# Equipe views
# view for creating equipe
def equipe_create(request):
    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipe_list")
    else:
        form = EquipeForm()
    return render(request, "equipe_create_form.html", {"form": form})


# view for listing equipes
def equipe_list(request):
    equipes = Equipe.objects.all()
    return render(request, "equipe_list.html", {"equipes": equipes})


# view for editing equipes
def equipe_edit(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == "POST":
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect("equipe_list")
    else:
        form = EquipeForm(instance=equipe)
    return render(request, "equipe_edit_form.html", {"form": form, "equipe": equipe})


# view for deleting equipes
def equipe_delete(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == "POST":
        equipe.delete()
        return redirect("equipe_list")


# Joueur Views


# view for creating joueur
def joueur_create(request):
    choices = Joueur.Post.choices
    equipes = Equipe.objects.all()
    if request.method == "POST":
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("joueur_list")
        else:
            print("form is not valid")
            print(form.errors)
            return render(
                request,
                "joueur_create_form.html",
                {"form": form, "choices": choices, "equipes": equipes},
            )

    else:
        form = JoueurForm()

    return render(
        request,
        "joueur_create_form.html",
        {"form": form, "choices": choices, "equipes": equipes},
    )


# view for listing joueurs
def joueur_list(request):
    joueurs = Joueur.objects.all()
    return render(request, "joueur_list.html", {"joueurs": joueurs})


# view for editing joueurs
def joueur_edit(request, pk):
    joueur = get_object_or_404(Joueur, pk=pk)
    choices = Joueur.Post.choices
    equipes = Equipe.objects.all()
    if request.method == "POST":
        form = JoueurForm(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
            return redirect("joueur_list")
    else:
        form = JoueurForm(instance=joueur)
    return render(
        request,
        "joueur_edit_form.html",
        {"form": form, "choices": choices, "joueur": joueur, "equipes": equipes},
    )


# view for deleting joueurs
def joueur_delete(request, pk):
    joueur = get_object_or_404(Joueur, pk=pk)
    if request.method == "POST":
        joueur.delete()
        return redirect("joueur_list")


# Match view


# create match view
def match_create(request):
    equipes = Equipe.objects.all()
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()

            update_equipes_points(
                form.cleaned_data["equipe_1"],
                form.cleaned_data["equipe_2"],
                form.cleaned_data["score_equipe_1"],
                form.cleaned_data["score_equipe_2"],
            )
            return redirect("match_list")
        else:
            print(form.errors)
            return render(
                request, "match_create_form.html", {"form": form, "equipes": equipes}
            )
    else:
        form = MatchForm()
    return render(request, "match_create_form.html", {"form": form, "equipes": equipes})


def match_list(request):
    matches = Match.objects.all()
    return render(request, "match_list.html", {"matches": matches})


def match_edit(request, pk):
    equipes = Equipe.objects.all()
    match = get_object_or_404(Match, pk=pk)
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()

            update_equipes_points(
                form.cleaned_data["equipe_1"],
                form.cleaned_data["equipe_2"],
                form.cleaned_data["score_equipe_1"],
                form.cleaned_data["score_equipe_2"],
            )
            return redirect("match_list")
        else:
            return render(
                request,
                "match_edit_form.html",
                {"form": form, "match": match, "equipes": equipes},
            )
    else:
        form = MatchForm(instance=match)
    return render(
        request,
        "match_edit_form.html",
        {"form": form, "match": match, "equipes": equipes},
    )


def match_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == "POST":

        # if the match is deleted
        update_equipes_points(
            match.equipe_1,
            match.equipe_2,
            match.score_equipe_1,
            match.score_equipe_2,
            match_deleted=True,
        )
        match.delete()

        return redirect("match_list")


# vue pour le classement


def classement(request):
    equipes = Equipe.objects.all().order_by("-points", "-buts_marques")
    return render(request, "classement.html", {"equipes": equipes})
