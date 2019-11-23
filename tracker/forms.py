from django import forms

class projectForm(forms.Form):
    name = forms.CharField(max_length=32, blank=True, null=False)
    description = forms.CharField(max_length=256, blank=True, null=False)
    ownerEmail = forms.EmailField(max_length=254)