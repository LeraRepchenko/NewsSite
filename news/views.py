from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

def index(request):
    news = News.objects.all()

    context = {
        'news': news,
        'title': 'Список новостей',

    }

    def news(request):
        return HttpResponse("Hello")
    return render(request, 'news/index.html', context)
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news,
                                                  'category': category})
def news(request):
    return HttpResponse("Hello")


def test(request):
    return HttpResponse("<h1>Тестовая страница<h1>")
# Create your views here.
