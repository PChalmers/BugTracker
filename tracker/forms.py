from django import forms

from .models import project, account, record, recordComment


class projectForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    Email = forms.EmailField()

class accountModelForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ['name', 'description', 'email', 'priority']


class projectModelForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ['name', 'description', 'owner']


class recordModelForm(forms.ModelForm):
    class Meta:
        model = record
        fields = ['projectId', 'type', 'status', 'title', 'description', 'originator', 'assigned']


class commentModelForm(forms.ModelForm):
    class Meta:
        model = recordComment
        fields = ['title', 'content', 'owner']

