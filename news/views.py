from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm


def add_news(request):

    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        form = NewsForm(request.POST)

        if form.is_valid():

            #news = News.objects.create(**form.cleaned_data)
            news = form.save

            return redirect('view_news', news_id=news.pk)

    return render(request, 'news/add_news.html', {'form': form})

def view_news(request, news_id):
    #news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})


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
