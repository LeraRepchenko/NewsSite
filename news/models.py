from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,
                             verbose_name='Наименование категории', blank=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['title', ]


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория', )
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def my_fune(self):
        return "Последние новости"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at', ]


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', verbose_name='Новость')
    author = models.CharField(max_length=100, verbose_name='Автор')
    email = models.EmailField(verbose_name='Email', blank=True)
    text = models.TextField(verbose_name='Текст комментария')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name='IP адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies',
                               verbose_name='Ответ на')

    def __str__(self):
        return f'{self.author}: {self.text[:50]}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']