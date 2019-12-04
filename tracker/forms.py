from django import forms

from .models import project, account, record, recordComment

class accountModelForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ['user', 'name', 'description', 'status']


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
        fields = ['recordID', 'title', 'recordID', 'content', 'owner']

