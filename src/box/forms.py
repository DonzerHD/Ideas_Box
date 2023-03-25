from django import forms
from box.models import Ideas_Box

class IdeasBoxForm(forms.ModelForm):
    """
    Form to create or update an Ideas_Box instance
    """
    class Meta:
        # Specify the model to be used for this form
        model = Ideas_Box
        # Specify the fields to be included in the form
        fields = ['title', 'description']
        # Specify the labels to be used for the form fields
        labels = {
            'title': 'Titre',
            'description': 'Description'
        }
        # Specify the widget for the "description" field
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

