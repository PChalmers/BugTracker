from django import forms

class projectForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    Email = forms.EmailField()