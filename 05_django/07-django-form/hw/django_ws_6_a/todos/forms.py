from django import forms 
from .models import Todo

class TodoForm(forms.Form):
  class Meta:
    model = Todo
    field = '__all__'