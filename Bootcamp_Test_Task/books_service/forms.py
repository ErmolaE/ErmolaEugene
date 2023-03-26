from django import forms
from django.core.exceptions import ValidationError
from .models import Book, Author, Genre, Language


# class AddBook(forms.Form):

#     title = forms.CharField(max_length=200, label='Title')
#     author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), widget=forms.CheckboxSelectMultiple, label='Authors')
#     summary = forms.CharField(widget=forms.Textarea, max_length=1000, label='Book description')
#     isbn = forms.CharField(max_length=13, label='ISBN')
#     genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple, label="Select a genre for this book")
#     language = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), widget=forms.CheckboxSelectMultiple, label='Language')
    
#     def clean_isbn(self):
#         t = self.cleaned_data['isbn']
#         if len(t) != 13:
#             raise ValidationError("Incorrect ISBN!")

#         return t

# class AddAuthor(forms.Form):

#     first_name = forms.CharField(max_length=100, label='first name')
#     last_name = forms.CharField(max_length=100, label='last name')
#     date_of_birth = forms.DateField(label='date of birth')
#     date_of_death = forms.DateField(label='date of death')
