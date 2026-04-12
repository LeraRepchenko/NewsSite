
from django.urls import path
from . import views
from .views import get_category

urlpatterns = [
    path('', views.index, name='home'),
    path('test', views.test),
    path('news', views.news),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', views.view_news, name='view_news'),
path('add-news/', views.add_news, name='add_news'),
]
