from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg border-0 add-todo-input bg-transparent rounded'}))


