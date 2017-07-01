from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='plz not empty query', widget=forms.TextInput(attrs={'size': 32}) )
