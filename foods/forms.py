from statistics import mode
from django import forms
from django.forms import ModelForm
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'pic_file', 'description', 'ingredients']