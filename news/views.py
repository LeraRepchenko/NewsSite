from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .utils import MyMixin, OrderByDateMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

def test_pagination(request):
    objects = ["john1", "paul2", "george3", "ringo4", "john5", "paul6", "george7"]
    paginator = Paginator(objects, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/test.html', {'page_obj': page_obj})


class HomeNews(OrderByDateMixin, MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.mixin_prop
        context['last_news'] = News.objects.filter(
            is_published=True
        ).order_by('-created_at')[:5]
        return context

class NewsByCategory(OrderByDateMixin, MyMixin, ListView):
    model = News
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 3
    template_name = 'news/home_news_list.html'

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs['category_id'],
            is_published=True
        ).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(pk=self.kwargs['category_id'])
        context['title'] = self.get_upper(category)
        context['last_news'] = News.objects.filter(
            is_published=True
        ).order_by('-created_at')[:5]
        return context

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'news/view_news.html'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'
    # raise_exception = True


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

class DeleteNews(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = News
        success_url = reverse_lazy('home')
        template_name = 'news/delete_news.html'
        raise_exception = True

        def test_func(self):
            return self.request.user.is_superuser



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