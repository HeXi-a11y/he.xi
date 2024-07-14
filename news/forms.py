from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','desc','fullText','date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'desc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Дата'
            }),
            'fullText': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),

        }