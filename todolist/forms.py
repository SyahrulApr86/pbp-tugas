from django.forms import ModelForm
from todolist.models import Task
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user', 'is_finished']
        

        widgets = {
            'date': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'title': forms.TextInput({'class': 'form-control'}),
            'description': forms.Textarea({'class': 'form-control'}),
        }