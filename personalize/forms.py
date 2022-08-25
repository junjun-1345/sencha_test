from django import forms


class DiagnoseForm(forms.Form):
    name = forms.CharField(max_length=100)