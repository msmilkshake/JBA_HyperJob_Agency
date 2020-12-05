from django import forms


class CreateForm(forms.Form):
    description = forms.CharField(label='Description')
