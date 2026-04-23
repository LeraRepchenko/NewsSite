
from django.urls import path
from . import views
#from .views import get_category

urlpatterns = [
    path('', views.HomeNews.as_view(), name='home'),
    path('test', views.test),
    path('news', views.news),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', views.ViewNews.as_view(), name='view_news'),
    path('add_news/', views.CreateNews.as_view(), name='add_news'),
    path('last/', views.LastNews.as_view(), name='last_news'),
]
