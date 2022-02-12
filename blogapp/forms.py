from django import forms
from . import models


class CreateArticle(forms.ModelForm):


    class Meta:
        model=models.Articles
        fields=['title', 'subtitle', 'body', 'thumb', 'category']
    

    category=forms.ModelMultipleChoiceField(queryset=models.Categories.objects.all(), widget=forms.CheckboxSelectMultiple)


class CreateCategory(forms.ModelForm):


    class Meta:
        model=models.Categories
        fields=['name', 'thumb']

