from django import forms


class DiagnoseForm(forms.Form):
    # keyword = forms.CharField(label='keyword', max_length=25)
    keyword0 = forms.BooleanField(label='keyword0', required=False)
    keyword1 = forms.BooleanField(label='keyword1', required=False)
    keyword2 = forms.BooleanField(label='keyword2', required=False)
    keyword3 = forms.BooleanField(label='keyword3', required=False)
    keyword4 = forms.BooleanField(label='keyword4', required=False)
    keyword5 = forms.BooleanField(label='keyword5', required=False)
    keyword6 = forms.BooleanField(label='keyword6', required=False)
    keyword7 = forms.BooleanField(label='keyword7', required=False)
    keyword8 = forms.BooleanField(label='keyword8', required=False)
    keyword9 = forms.BooleanField(label='keyword9', required=False)
