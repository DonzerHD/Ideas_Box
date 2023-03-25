from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def logout_user(request):
    """
    Log out the user.
    """
    logout(request)
    return redirect('login')

def login_view(request):
    """
    Handle the user login.
    """
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # Get the username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in and redirect to the index page
                login(request, user)
                return redirect('index')
            else:
                # Display an error message if the username or password is invalid
                message = "Password or invalid username"
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})  

def register(request):
    """
    Handle the user registration.
    """
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            # Get the username, password, and email from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            # Create a new user and log them in
            new_user = User.objects.create_user(username=username, password=password , email=email)
            login(request, new_user)

            # Redirect the user to the index page
            return redirect('index')
    else:
        form = forms.RegisterForm()

    return render(request, 'authentication/register.html', {'form': form})