# Apostolis: Create forms and render them

from django import forms
from .models import *


class PieceForm(forms.ModelForm):
    class Meta:
        model = PieceOfArt
        fields = ('name', 'creator', 'description', 'creation_year', 'image')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'rating')

