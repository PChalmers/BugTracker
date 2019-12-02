from django import forms

from .models import project


class projectForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Description = forms.CharField(widget=forms.Textarea)

class projectModelForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ['name', 'description', 'owner']

class recordForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Description = forms.CharField(widget=forms.Textarea)

class commentForm(forms.Form):
    Title = forms.CharField()
    Comment = forms.CharField(widget=forms.Textarea)
    Email = forms.EmailField()






