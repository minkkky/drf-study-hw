from tkinter import CASCADE
from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Article(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    content = models.TextField('본문')
    created_at = models.DateTimeField(auto_now_add=True)
    exposure_start_date = models.DateField("노출 시작 일자", default=timezone.now)
    exposure_end_date = models.DateField("노출 종료 일자", default=timezone.now)

    def __str__(self):
        return f'{self.title} ({self.author})'

class Comment(models.Model):
    article = models.ForeignKey(Article,  on_delete=models.CASCADE)
    user = models.ForeignKey('user.User',  on_delete=models.CASCADE)
    content = models.TextField('본문')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.article.id}] {self.content} by {self.user.username}'