from pyexpat.errors import messages
from django.db import IntegrityError
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from box.forms import IdeasBoxForm
from box.models import Ideas_Box, Vote

# Create your views here.
@login_required
def create_ideas_box(request):
    if request.method == 'POST':
        form = IdeasBoxForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')

            # Créer une nouvelle boîte d'idées
            new_ideas_box = Ideas_Box(title=title, description=description, createur=request.user)
            new_ideas_box.save()
            return redirect('index')
    else:
        form = IdeasBoxForm()

    return render(request, 'box/create_box.html', {'form': form})

@login_required
def lists_box(request):
    boxs = Ideas_Box.objects.all()
    user_votes = Vote.objects.filter(user=request.user).values_list('box', flat=True)
    return render(request, 'box/list_box.html', {'boxs': boxs, 'user_votes': user_votes})

@login_required
def vote(request, box_id):
    box = get_object_or_404(Ideas_Box, id=box_id)

    try:
        vote = Vote(user=request.user, box=box)
        vote.save()

        box.votes += 1
        box.save()
    except IntegrityError:
        # L'utilisateur a déjà voté pour cette idée
        pass

    return redirect('list_box')
