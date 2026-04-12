import re
from django import forms
from django.core.exceptions import ValidationError
from .models import News, Category


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category', 'photo']

        labels = {
            'title': 'Название',
            'content': 'Текст',
            'is_published': 'Опубликовано?',
            'category': 'Категория',
            'photo': 'Изображение',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and re.match(r'^\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title