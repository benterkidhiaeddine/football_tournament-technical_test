from django.shortcuts import render,redirect, get_object_or_404
from tournament.models import Equipe, Joueur
from tournament.forms import EquipeForm, JoueurForm
# Create your views here.


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
    return render(request, "equipe_confirm_delete.html", {"equipe": equipe})



# Joueur Views

# view for creating joueur
def joueur_create(request):
    choices = Joueur.Post.choices
    if request.method == "POST":
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("joueur_list")
        else:
            form.add_error(None, "Veuillez corriger les erreurs ci-dessous.")
            return render(request, "joueur_create_form.html", {"form": form, "choices": choices})
    else:
        form = JoueurForm()

    return render(request, "joueur_create_form.html", {"form": form, "choices": choices})


# view for listing joueurs
def joueur_list(request):
    joueurs = Joueur.objects.all()
    return render(request, "joueur_list.html", {"joueurs": joueurs})


# view for editing joueurs
def joueur_edit(request, pk):
    joueur = get_object_or_404(Joueur, pk=pk)
    choices = Joueur.Post.choices
    if request.method == "POST":
        form = JoueurForm(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
            return redirect("joueur_list")
        else:
            form.add_error(None, "Veuillez corriger les erreurs ci-dessous.")
            return render(request, "joueur_edit_form.html", {"form": form, "choices": choices})
    else:
        form = JoueurForm(instance=joueur)
    return render(request, "joueur_edit_form.html", {"form": form, "choices": choices , "joueur": joueur    })


# view for deleting joueurs
def joueur_delete(request, pk):
    joueur = get_object_or_404(Joueur, pk=pk)
    if request.method == "POST":
        joueur.delete()
        return redirect("joueur_list")
    return render(request, "joueur_confirm_delete.html", {"joueur": joueur})
