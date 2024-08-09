from django import forms
from tasks.models import Task
from categories.models import Category


class TaskForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'tags', 'completed', 'due_date', 'categories']
