
from django import template
from news.models import Category# noqa

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories(name='get_list_categories'):
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Последние новости'):
    categories = Category.objects.all()
    return {'categories': categories, 'arg1': arg1, }