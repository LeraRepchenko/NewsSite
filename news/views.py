from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['last_news'] = News.objects.filter(
            is_published=True
        ).order_by('-created_at')[:5]
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    allow_empty = False
    extra_context = {'title': 'Категория'}

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs['category_id'],
            is_published=True
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(pk=self.kwargs['category_id'])
        context['title'] = category.title
        context['last_news'] = News.objects.filter(
            is_published=True
        ).order_by('-created_at')[:5]
        return context


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'news/view_news.html'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')


class LastNews(ListView):
    model = News
    template_name = 'news/last_news.html'
    context_object_name = 'last_news'

    def get_queryset(self):
        return News.objects.filter(
            is_published=True
        ).order_by('-created_at')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Последние новости'
        return context



# def add_news(request):
#     form = NewsForm()
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             news = form.save()
#             return redirect('view_news', news_id=news.pk)
#     return render(request, 'news/add_news.html', {'form': form})


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})


def news(request):
    return HttpResponse("Hello")


def test(request):
    return HttpResponse("<h1>Тестовая страница<h1>")