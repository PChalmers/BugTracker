from django import forms


class projectForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Description = forms.CharField(widget=forms.Textarea)

class recordForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Description = forms.CharField(widget=forms.Textarea)

class commentForm(forms.Form):
    Title = forms.CharField()
    Comment = forms.CharField(widget=forms.Textarea)
    Email = forms.EmailField()






