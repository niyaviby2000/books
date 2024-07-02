from django import forms

class BookForm(forms.Form):

    title=forms.CharField()

    year=forms.IntegerField()

    author=forms.CharField()

    genre=forms.CharField()

    language=forms.CharField()