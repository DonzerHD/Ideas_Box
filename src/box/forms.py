from django import forms

from box.models import Ideas_Box

class IdeasBoxForm(forms.ModelForm):
    class Meta:
        model = Ideas_Box
        fields = ['title', 'description']
        labels = {
            'title': 'Titre',
            'description': 'Description'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

