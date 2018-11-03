from django import forms
from .models import Todo

class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'due_date': DateInput()
        }
