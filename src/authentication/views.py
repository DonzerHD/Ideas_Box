from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def logout_user(request):
    """Déconnexion de l'utilisateur"""
    logout(request)
    return redirect('login')

def login_view(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = "Password or invalid username"
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})  


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            # Créer un nouvel utilisateur
            new_user = User.objects.create_user(username=username, password=password , email=email)

            # Connecter l'utilisateur nouvellement créé
            login(request, new_user)

            # Rediriger l'utilisateur vers la page d'accueil
            return redirect('index')
    else:
        form = forms.RegisterForm()

    return render(request, 'authentication/register.html', {'form': form})