from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    A form for user login
    """
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    """
    A form for user registration
    """
    username = forms.CharField(label="Username")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
    
    def clean_username(self):
        """
        Validate that the username is unique
        """
        # Retrieve the username from cleaned data
        username = self.cleaned_data['username']
        # Check if a user with the same username already exists in the database
        if User.objects.filter(username=username).exists():
            # Raise a validation error if a user with the same username exists
            raise forms.ValidationError("Username already used")
        # Return the cleaned username
        return username
    
    def clean_email(self):
        """
        Validate that the email is unique
        """
        # Retrieve the email from cleaned data
        email = self.cleaned_data['email']
        # Check if a user with the same email already exists in the database
        if User.objects.filter(email=email).exists():
            # Raise a validation error if a user with the same email exists
            raise forms.ValidationError("Email already used")
        # Return the cleaned email
        return email
    
    def clean(self):
        """
        Validate that the passwords match
        """
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2 or password2 != password1:
            self.add_error("password2", "Passwords do not match.")