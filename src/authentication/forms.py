from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
    username = forms.CharField(label="Username")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already used")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already used")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2 or password2 != password1:
            self.add_error("password2", "Passwords do not match.")