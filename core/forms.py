from django import forms
from core.models import FastNote


class FastNoteForm(forms.ModelForm):
    class Meta:
        model = FastNote
        fields = ['content']